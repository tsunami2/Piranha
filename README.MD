# Fish Audio Wyoming TTS

## Description
Orale, homes! This is a Home Assistant TTS integration using Fish.Audio and the Wyoming protocol. It lets your smart home assistant talk firme, responding with that Cholo flavor.

## Installation

### Step 1: Add Repository to HACS
1. Open Home Assistant and go to **HACS**.
2. Click on **Integrations**.
3. Click the three dots in the top-right corner and select **Custom repositories**.
4. Add the following repository URL:
   ```
   https://github.com/tsunami/piranha
   ```
5. Select **Integration** as the category and click **Add**.

### Step 2: Install the Integration
1. After adding the repo, go to **HACS > Integrations**.
2. Search for **Fish Audio Wyoming TTS**.
3. Click **Download** and install the integration.
4. Restart Home Assistant.

### Step 3: Configure the Integration
1. Go to **Settings > Devices & Services**.
2. Click **Add Integration** and search for **Fish Audio Wyoming TTS**.
3. Follow the setup instructions to configure it with your Fish.Audio API key.

## Usage
Use the TTS service in Home Assistant to make your assistant speak Cholo-style:
```yaml
service: tts.speak
data:
  entity_id: media_player.your_speaker
  message: "What's up, ese?"
```

## Features
✅ Uses Wyoming protocol for seamless integration  
✅ Generates speech through Fish.Audio API  
✅ Adds firme Cholo-style responses  
✅ Works with Home Assistant's TTS service

## Support
If you run into issues, drop a message in the repo or open an issue, homes!

Orale, happy automating, ese! 🚗💨

