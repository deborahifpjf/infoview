# InfoView

InfoView is a Python-based application designed to manage sound settings and equalize audio output for different media types on Windows. Whether you're listening to music, watching movies, playing games, or engaging in voice calls, InfoView helps optimize your audio experience by adjusting system volume and equalizer settings.

## Features

- Change system volume level
- Adjust equalizer settings based on media type
- Support for media types: Music, Movies, Games, Voice

## Requirements

- Python 3.x
- Windows OS
- [NirCmd](https://www.nirsoft.net/utils/nircmd.html) utility for volume control (ensure it is in your system's PATH)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/InfoView.git
   ```

2. Navigate to the project directory:
   ```bash
   cd InfoView
   ```

3. Ensure you have [NirCmd](https://www.nirsoft.net/utils/nircmd.html) installed and accessible from your command line.

## Usage

To run InfoView, use the following command:

```bash
python InfoView.py [media_type] [volume_level]
```

- `media_type`: The type of media you're optimizing audio for. Options are `music`, `movie`, `game`, or `voice`.
- `volume_level`: The desired system volume level (0-65535). Default is 50000 if not specified.

### Example

```bash
python InfoView.py music 30000
```

This command sets the system volume to 30000 and applies the equalizer settings for music.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

```

Note: This code includes a simulated volume change using the NirCmd utility, which would need to be installed separately and available in your system's PATH.