> In July 2025, I began a new career as a software engineer. I stare at the terminal for hours, producing output like a machine but slowly losing focus inside. What I truly needed was not another productivity tool, but a small moment of pause ---- a gentle reminder that I am human before I am a worker.
>
> Terminal Zen grew out of that realization. It disguises rest as code: a simple progress bar that guides your breath while looking like just another script running. There is no flashy UI, only a minimal intervention that fits quietly into the environment where exhaustion often happens.


<div align="center">
  <img src="Terminal Zen.png" alt="Terminal Zen" width="100%">
</div>

# Terminal Zen 🧘

A minimal, terminal-based breathing and meditation guide with ASCII progress bars. Perfect for quick mindfulness sessions during your coding breaks.

## Features

- **Zero Dependencies**: Uses only Python standard library
- **Interactive Mode**: Choose from 1, 3, or 10-minute guided sessions
- **Configurable Breathing**: Customize inhale, hold, and exhale durations
- **Visual Progress**: ASCII progress bars with directional breathing guidance
- **Flexible Duration**: Support for seconds, minutes, and hours
- **Graceful Exit**: Exit anytime with `q`, `Esc`, or `Ctrl+C`
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Philosophical Wisdom**: Random philosophical quotes upon completion

## Installation

### Option 1: Homebrew (Recommended for macOS)

```bash
# Add the tap (only needed once)
brew tap bobtianqiwei/tap

# Install terminal-zen
brew install terminal-zen
```

> **Note**: If you haven't set up the Homebrew tap yet, you can also install directly from the repository:
> ```bash
> brew install bobtianqiwei/terminal-zen/terminal-zen
> ```

### Option 2: pipx (Cross-platform)

#### First time setup (if you don't have pipx)

```bash
# Install pipx
pip install pipx

# Add pipx to your PATH
pipx ensurepath

# Restart your terminal or run: source ~/.bashrc (or ~/.zshrc)
```

#### Install Terminal Zen

```bash
pipx install git+https://github.com/bobtianqiwei/terminal-zen.git
```

## Usage

### Interactive Mode (Recommended)

```bash
zen
```

This will present you with three options:
- **Quick Relaxation** (1 minute) - Perfect for coding breaks
- **Standard Meditation** (3 minutes) - Daily stress relief
- **Deep Meditation** (10 minutes) - Extended mindfulness practice

### Command Line Mode

```bash
# Default 60-second session (7s inhale, 3s hold, 7s exhale, 3s hold)
zen --duration 60s

# 2-minute session
zen --duration 2m

# Custom breathing pattern
zen --inhale 5 --hold1 3 --exhale 5 --hold2 3

# View help
zen --help
```

## Demo

Here's what a typical interactive session looks like:

```
Terminal Zen - Choose Your Meditation Mode
========================================================
1. Quick Relaxation (1 minute)
2. Standard Meditation (3 minutes)
3. Deep Meditation (10 minutes)
0. Exit
========================================================
Please select a mode (1-3, 0 to exit): 1

Quick Relaxation - Getting Ready
========================================================
Preparation Tips:
   • Find a quiet, comfortable place
   • Sit up straight, relax your shoulders
   • Close your eyes or focus on the screen
   • Get ready to follow the breathing rhythm

Press Enter when you're ready to begin...

========================================================
Terminal Zen - Breathing Guide
Press 'q', 'Esc', or Ctrl+C to exit
Session duration: 1m 0s
Cycle: Inhale 7s, Hold 3s, Exhale 7s, Hold 3s
--------------------------------------------------------
Starting in 0s: ████████████████████████████████████████    
Begin!

Cycle 1
Inhale  : ████████████████████████████████████████
Hold    : ████████████████████████████████████████
Exhale  : ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Hold    : ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

========================================================
🌿 'The mind is everything. What you think you become.' — Buddha
========================================================
Terminal Zen by Bob Tianqi Wei
GitHub: https://github.com/bobtianqiwei
========================================================
```

## Command Line Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--duration` | `-d` | `60s` | Session duration (e.g., `30s`, `2m`, `1h`) |
| `--inhale` | `-i` | `7` | Inhale duration in seconds |
| `--hold1` | `-H1` | `3` | Hold duration after inhale in seconds |
| `--exhale` | `-e` | `7` | Exhale duration in seconds |
| `--hold2` | `-H2` | `3` | Hold duration after exhale in seconds |
| `--fps` | `-f` | `10` | Progress bar refresh rate (1-60) |

## Features in Detail

### Progress Bar Direction
- **Inhale**: Progress bar fills from left to right
- **Hold**: Progress bar remains static (maintains previous state)
- **Exhale**: Progress bar empties from right to left
- **Hold**: Progress bar remains static (maintains previous state)

### Philosophical Wisdom
Upon completing a session, you'll receive a random philosophical quote from various traditions:
- Eastern Philosophy (Buddhism, Zen)
- Ancient Chinese Philosophy (Confucius, Laozi, Zhuangzi)
- Modern Western Philosophy

### Interactive Experience
- Preparation guide with mindfulness tips
- 10-second countdown before starting
- Real-time breathing guidance
- Completion celebration with wisdom

## Requirements

- Python 3.9 or higher
- No external dependencies (uses only standard library)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Bob Tianqi Wei** - [GitHub](https://github.com/bobtianqiwei)

## Development

For information about setting up Homebrew installation, see [HOMEBREW_SETUP.md](HOMEBREW_SETUP.md).

---

Take a moment to breathe. Your code can wait. 🧘‍♂️
