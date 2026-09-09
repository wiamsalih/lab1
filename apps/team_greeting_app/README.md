
## Launch Steps

**Terminal 1: Simulation daemon**
```powershell
C:\Users\nopha\reachy_mini_env\Scripts\Activate.ps1
reachy-mini-daemon --sim
```
Leave running. Wait for the 3D viewer window to open.

**Terminal 2: App**
```powershell
C:\Users\nopha\reachy_mini_env\Scripts\Activate.ps1
cd C:\Users\nopha\lab1\apps\team_greeting_app
python -m team_greeting_app.main
```
Wait for: `Uvicorn running on http://0.0.0.0:8042`

**Browser**
```
http://localhost:8042
```
Click **👋 Say Hi** to watch the robot move in the 3D viewer window.

**Stop**
- `Ctrl+C` in Terminal 2 (app)
- `Ctrl+C` in Terminal 1 (daemon)
