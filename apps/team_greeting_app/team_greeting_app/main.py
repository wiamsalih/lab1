import threading
import time
from datetime import datetime

import numpy as np
from fastapi.responses import HTMLResponse
from reachy_mini import ReachyMini, ReachyMiniApp
from reachy_mini.utils import create_head_pose


class TeamGreetingApp(ReachyMiniApp):
    custom_app_url: str | None = "http://0.0.0.0:8042"
    request_media_backend: str | None = None

    ORIENT_YAW_DEG: float = 25.0
    ORIENT_DURATION_S: float = 1.0
    TILT_ROLL_DEG: float = 15.0
    GREETING_DURATION_S: float = 3.0
    ANTENNA_AMPLITUDE_DEG: float = 30.0
    LOOP_INTERVAL_S: float = 0.02
    NEUTRAL_DURATION_S: float = 1.0
    IDLE_POLL_S: float = 0.05

    def _log(self, stage: str) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] {stage}")

    def run(self, reachy_mini: ReachyMini, stop_event: threading.Event) -> None:
        greet_requested = threading.Event()

        @self.settings_app.get("/", response_class=HTMLResponse)
        def index() -> str:
            return HTML_PAGE

        @self.settings_app.post("/greet")
        def trigger_greet() -> dict:
            greet_requested.set()
            return {"status": "ok"}

        neutral_pose = create_head_pose(yaw=0.0, roll=0.0, degrees=True)
        reachy_mini.set_target(head=neutral_pose, antennas=np.array([0.0, 0.0]))
        self._log("SLEEP - waiting for button press")

        while not stop_event.is_set():
            if greet_requested.wait(timeout=self.IDLE_POLL_S):
                greet_requested.clear()
                self._run_greeting_sequence(reachy_mini, stop_event)
                if not stop_event.is_set():
                    self._log("SLEEP - waiting for button press")

        self._log("DONE - team_greeting_app stopped")

    def _run_greeting_sequence(
        self, reachy_mini: ReachyMini, stop_event: threading.Event
    ) -> None:
        self._log("STAGE 1/3 - Orienting toward user")
        orient_pose = create_head_pose(yaw=self.ORIENT_YAW_DEG, degrees=True)
        reachy_mini.set_target(head=orient_pose, antennas=np.array([0.0, 0.0]))
        if stop_event.wait(timeout=self.ORIENT_DURATION_S):
            return

        self._log("STAGE 2/3 - Greeting (head tilt + antennas)")
        t0 = time.time()
        while not stop_event.is_set():
            t = time.time() - t0
            if t >= self.GREETING_DURATION_S:
                break

            roll_deg = self.TILT_ROLL_DEG * np.sin(2.0 * np.pi * 0.7 * t)
            head_pose = create_head_pose(
                yaw=self.ORIENT_YAW_DEG, roll=roll_deg, degrees=True
            )

            antenna_deg = self.ANTENNA_AMPLITUDE_DEG * np.sin(2.0 * np.pi * 2.0 * t)
            antennas_rad = np.deg2rad(np.array([antenna_deg, -antenna_deg]))

            reachy_mini.set_target(head=head_pose, antennas=antennas_rad)

            if stop_event.wait(timeout=self.LOOP_INTERVAL_S):
                return

        self._log("STAGE 3/3 - Returning to neutral (sleep)")
        neutral_pose = create_head_pose(yaw=0.0, roll=0.0, degrees=True)
        reachy_mini.set_target(head=neutral_pose, antennas=np.array([0.0, 0.0]))
        stop_event.wait(timeout=self.NEUTRAL_DURATION_S)


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Reachy Mini - Greeting</title>
<style>
  body {
    margin: 0;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #1b1c22;
    font-family: -apple-system, Segoe UI, Roboto, sans-serif;
  }
  button#greetBtn {
    padding: 22px 44px;
    font-size: 20px;
    font-weight: 600;
    color: white;
    background: linear-gradient(135deg, #6c5ce7, #00cec9);
    border: none;
    border-radius: 999px;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(108, 92, 231, 0.4);
    transition: transform 0.12s ease, box-shadow 0.12s ease;
  }
  button#greetBtn:hover { transform: translateY(-2px); }
  button#greetBtn:active {
    transform: translateY(1px) scale(0.98);
    box-shadow: 0 4px 12px rgba(108, 92, 231, 0.4);
  }
  button#greetBtn:disabled {
    opacity: 0.6;
    cursor: default;
    transform: none;
  }
  #status {
    position: fixed;
    bottom: 24px;
    color: #9aa0a6;
    font-size: 14px;
  }
</style>
</head>
<body>
  <button id="greetBtn">👋 Say Hi</button>
  <div id="status"></div>
  <script>
    const btn = document.getElementById('greetBtn');
    const status = document.getElementById('status');
    btn.addEventListener('click', async () => {
      btn.disabled = true;
      status.textContent = 'Greeting...';
      try {
        await fetch('/greet', { method: 'POST' });
      } catch (e) {
        status.textContent = 'Could not reach robot.';
      }
      setTimeout(() => {
        btn.disabled = false;
        status.textContent = '';
      }, 5000);
    });
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    app = TeamGreetingApp()
    try:
        app.wrapped_run()
    except KeyboardInterrupt:
        app.stop()