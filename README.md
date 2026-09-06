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

## 3: Run App in Simulation Mode

**Application:** `reachy_mini_conversation_app`  
**Interaction tested:** `Simple greeting and conversation, asking for a short dance.`

[▶️ Watch the Reachy conversation demo](Images/reachy-conversation.mp4)

## User Interaction

- **Expected:** `The application expects the user to greet Reachy and engage in a simple conversation.`
- **Observed:** `I greeted Reachy, asked how it felt, and then unexpectedly requested that it dance.`
- **Robot behaviour:** `Reachy responded quickly and appropriately throughout the interaction. Despite the unexpected dance request, it successfully executed the action without failing or requiring additional clarification.`
- **Differences:** `The only unexpected response occurred when I greeted the robot as "Reachy." It added the statement "Reachy works for me too" after the greeting, which was somewhat confusing because the meaning of the statement was unclear in the context of the interaction.`

## Simulator Strengths

- `The Reachy Mini responded quickly and used natural-looking movements and expressions, making the interaction feel smooth and intuitive. The simulator also provided access to the robot's camera, speaker, and microphone, allowing it to respond to environmental and conversational inputs in a way that approximated an interactive HRI experience.`

## Simulator Limitations

- **Physical/environmental interaction:** `The simulator does not support free physical movement through the environment, limiting the evaluation of how Reachy would navigate physical space or interact with objects and people around it.`
- **Interaction memory/context:** `The simulator appeared limited in maintaining conversational or interaction context. For example, I prompted the robot to look left and move its antennas. When I subsequently said "look again," it returned an error indicating that it did not understand what I meant. This limits the ability to evaluate how effectively the robot maintains context during an ongoing HRI interaction.`

## 3.3 Teleoperation in Simulation mode
| neutral | two expressive channels |
|---|---|
| ![neutral](Images/neutral.png) | ![two expressive channels](Images/twoexpressivechannels.png) |
# Creating & Running App

# Testing / Observing / Reflecting
