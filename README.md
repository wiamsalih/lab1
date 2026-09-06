# Lab 1: Introduction to Reachy Mini

### Team Members: Nophar Shalom, Wiam Salih, Bailey Carlson

## 1: Setup Record
| Team Member | Operating System and Architecture  | Reachy Mini Control Version | Installation Issue / Resolution  |
|-------------|------------------------------------|-----------------------------|----------------------------------|
|   Nophar    |            Windows 11              |           v0.9.34           |               N/A                |
|   Bailey    |        macOS 15.7.3, ARM64         |           v0.9.34           |               N/A                |
|   Wiam      |                                    |                             |                                  |


## 2: Reachy Mini in Simulation Mode

<img src="Images/ReachyMiniSimulationWindow.png" alt="Reachy Mini setup" width="500">

## 2.5: Reachy Mini Conversation App Run

<img src="Images/ReachyMiniConvoAppScreenshot.png" alt="Reachy Mini Convo App" width="500">

# 3: Run App in Simulation Mode
## Application Interaction Cycle

**Application:** `reachy_mini_conversation_app`  
**Interaction tested:** `Simple greeting and conversation, asking for a short dance.`

[▶️ Watch the Reachy conversation demo](Images/reachy-conversation.mp4)

### User Interaction
- **Expected:** `The application expects the user to greet Reachy and have simple conversations`
- **Observed:** `I greeted Reachy, asked it how it feels, and requested it to dance.`
- **Application response:** `The application responded effectively and quickly, even with the unexpected dance request, it performed without fail.`
- **Differences:** `Only mismatch was when I greeted the Reachy Mini as 'Reachy' it added a sentence after the greeting saying "Reachy works for me too", which confused me slightly as to what it meant.`

### Simulator Strengths
- The Reachy Mini responds quickly and moves in the simulator with natural expressions, making the overall interaction feel smooth and intuitive. It has access to the camera, speaker, and microphone, so it is able to gain contextual awareness as if it was actually in the environment.

### Simulator Limitations
- Limitations of the simulator include a lack of free movement, which would have given the robot a much greater understanding of its environment and an enhanced way of interaction with its surroundings. Additionally, it seemed to lack memory; I prompted the robot to look left and move its antennas, and after that execution, when I said, look again, it responded with an error message, saying that it didn't know what I meant.

# Creating & Running App

# Testing / Observing / Reflecting
