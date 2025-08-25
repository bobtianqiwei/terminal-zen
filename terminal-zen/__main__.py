# terminal_zen/__main__.py developed by Bob Tianqi Wei

"""
Main CLI entry point for Terminal Zen.

Provides breathing guidance with ASCII progress bars and configurable timing.
"""

import argparse
import signal
import sys
import time
import threading
import random
from typing import Optional


class BreathingSession:
    """Manages a breathing session with progress visualization."""
    
    def __init__(self, duration: int, inhale: int, hold1: int, exhale: int, hold2: int, fps: int = 10):
        self.duration = duration
        self.inhale = inhale
        self.hold1 = hold1  # Hold after inhale
        self.exhale = exhale
        self.hold2 = hold2  # Hold after exhale
        self.fps = fps
        self.cycle_duration = inhale + hold1 + exhale + hold2
        self.running = False
        self.current_progress = 0.0  # Track current progress state
        
    def start(self):
        """Start the breathing session."""
        self.running = True
        self.setup_signal_handlers()
        
        start_time = time.time()
        cycle_count = 0
        
        while self.running and (time.time() - start_time) < self.duration:
            cycle_count += 1
            print(f"\nCycle {cycle_count}")
            
            # Inhale phase - progress bar goes right
            if not self.run_phase("Inhale  ", self.inhale, show_progress=True, reverse=False):
                break
                
            # Hold phase 1 - static progress bar (keep inhale progress at 100%)
            self.current_progress = 1.0  # Ensure we keep the full progress from inhale
            if not self.run_phase("Hold    ", self.hold1, show_progress=False, keep_progress=True):
                break
                
            # Exhale phase - progress bar goes left
            if not self.run_phase("Exhale  ", self.exhale, show_progress=True, reverse=True):
                break
                
            # Hold phase 2 - static progress bar (keep exhale progress at 0%)
            self.current_progress = 0.0  # Ensure we keep the empty progress from exhale
            if not self.run_phase("Hold    ", self.hold2, show_progress=False, keep_progress=True):
                break
        
        if self.running:
            print("\n" + "=" * 56)
            print(get_random_completion_message())
            print("=" * 56)
            print("Terminal Zen by Bob Tianqi Wei")
            print("GitHub: https://github.com/bobtianqiwei")
            print("=" * 56)
        else:
            print("\nSession interrupted.")
    
    def run_phase(self, phase_name: str, duration: int, show_progress: bool = True, reverse: bool = False, keep_progress: bool = False) -> bool:
        """Run a single breathing phase with optional progress bar."""
        if not self.running:
            return False
            
        if show_progress:
            # Phase with progress bar - use step-based approach for precise timing
            total_steps = duration * self.fps
            for step in range(int(total_steps) + 1):
                if not self.running:
                    return False
                    
                progress = step / total_steps
                if reverse:
                    progress = 1.0 - progress  # Reverse for exhale
                self.current_progress = progress  # Update current progress
                self.display_progress_bar(progress, phase_name)
                
                # Check for user input
                if self.check_exit_input():
                    return False
                    
                if step < total_steps:  # Don't sleep on the last step
                    time.sleep(1.0 / self.fps)
        else:
            # Phase without progress bar (hold phases)
            if keep_progress:
                # Keep the current progress bar state but show hold phase name
                self.display_progress_bar(self.current_progress, phase_name)
            else:
                # Show empty progress bar
                self.display_progress_bar(0.0, phase_name)
                
            start_time = time.time()
            target_end_time = start_time + duration
            
            while self.running and time.time() < target_end_time:
                # Check for user input
                if self.check_exit_input():
                    return False
                    
                time.sleep(1.0 / self.fps)
        
        return True
    
    def display_progress_bar(self, progress: float, phase_name: str):
        """Display ASCII progress bar."""
        bar_width = 40
        # Use round() for proper rounding instead of int() truncation
        filled_width = min(round(bar_width * progress), bar_width)
        bar = "█" * filled_width + "░" * (bar_width - filled_width)
        
        # Clear line and display progress (without brackets and percentage)
        print(f"\r{phase_name}: {bar}", end="", flush=True)
    
    def check_exit_input(self) -> bool:
        """Check for exit input without blocking."""
        import select
        
        if sys.platform == "win32":
            try:
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    if key in ['q', '\x1b']:  # q or Esc
                        self.running = False
                        return True
            except ImportError:
                pass
        else:
            # Unix-like systems
            if select.select([sys.stdin], [], [], 0)[0]:
                key = sys.stdin.read(1).lower()
                if key in ['q', '\x1b']:  # q or Esc
                    self.running = False
                    return True
        
        return False
    
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful exit."""
        def signal_handler(signum, frame):
            self.running = False
            print("\n\nSession interrupted by signal.")
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    @staticmethod
    def format_time(seconds: int) -> str:
        """Format seconds into human readable time."""
        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            return f"{minutes}m {remaining_seconds}s"
        else:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours}h {minutes}m"


def get_random_completion_message():
    """Get a random philosophical completion message."""
    messages = [
        # Eastern Philosophy (Buddhism, Zen)
        "🌿 'The mind is everything. What you think you become.' — Buddha",
        "🌅 'Peace comes from within. Do not seek it without.' — Buddha",
        "🌊 'Breathing in, I calm body and mind. Breathing out, I smile.' — Thich Nhat Hanh",
        "🌸 'The present moment is filled with joy and happiness. If you are attentive, you will see it.' — Thich Nhat Hanh",
        "🌙 'Your breathing is your greatest friend. Return to it in all your troubles and you will find comfort and guidance.' — Thich Nhat Hanh",
        "☀️ 'The present moment is the only time over which we have dominion.' — Thich Nhat Hanh",
        
        # Ancient Chinese Philosophy
        "🏔️ 'Knowing where to stop brings stability, stability brings tranquility, tranquility brings peace, peace brings reflection, reflection brings attainment.' — Confucius",
        "🌊 'The highest good is like water, which benefits all things without contention.' — Laozi",
        "🌙 'Attain the utmost in emptiness, hold fast to stillness.' — Laozi",
        "🌸 'When the mind is like still water, all things become clear.' — Zhuangzi",
        "🌿 'Not to be elated by external gains, not to be saddened by personal losses.' — Fan Zhongyan",
        "☀️ 'When sitting quietly, reflect on your own faults; when chatting idly, don't discuss others' wrongs.' — Ancient Chinese Proverb",
        "🌅 'The heart is like still water, undisturbed by waves.' — Ancient Chinese Proverb",
        
        # Modern Western Philosophy
        "🌱 'The quieter you become, the more you can hear.' — Ram Dass",
        "💎 'Meditation is the discovery that the point of life is always arrived at in the immediate moment.' — Alan Watts",
        "🌊 'Meditation is not a means to an end. It is both the means and the end.' — Jiddu Krishnamurti",
        "🌸 'The only way to live is by accepting each minute as an unrepeatable miracle.' — Tara Brach",
        "🌙 'Meditation is not about stopping thoughts, but recognizing that we are more than our thoughts and our feelings.' — Arianna Huffington",
        "☀️ 'In the midst of movement and chaos, keep stillness inside of you.' — Deepak Chopra"
    ]
    return random.choice(messages)


def show_mode_selection():
    """Show interactive mode selection."""
    print("Terminal Zen - Choose Your Meditation Mode")
    print("=" * 56)
    print("1. Quick Relaxation (1 minute)")
    print("2. Standard Meditation (3 minutes)")
    print("3. Deep Meditation (10 minutes)")
    print("0. Exit")
    print("=" * 56)
    
    while True:
        try:
            choice = input("Please select a mode (1-3, 0 to exit): ").strip()
            if choice == "0":
                print("Goodbye!")
                sys.exit(0)
            elif choice in ["1", "2", "3"]:
                return choice
            else:
                print("Invalid choice, please enter 1, 2, 3, or 0")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)


def get_session_config(choice: str):
    """Get session configuration based on user choice."""
    configs = {
        "1": {
            "duration": 60,
            "name": "Quick Relaxation",
            "description": "1-minute quick relaxation session"
        },
        "2": {
            "duration": 180,
            "name": "Standard Meditation", 
            "description": "3-minute standard meditation session"
        },
        "3": {
            "duration": 600,
            "name": "Deep Meditation",
            "description": "10-minute deep meditation session"
        }
    }
    return configs[choice]


def show_preparation_guide(mode_name: str, duration: int, session: BreathingSession):
    """Show preparation guide before starting the session."""
    print(f"\n{mode_name} - Getting Ready")
    print("=" * 56)
    
    if duration <= 60:
        print("Preparation Tips:")
        print("   • Find a quiet, comfortable place")
        print("   • Sit up straight, relax your shoulders")
        print("   • Close your eyes or focus on the screen")
        print("   • Get ready to follow the breathing rhythm")
    elif duration <= 180:
        print("Preparation Tips:")
        print("   • Find a quiet, comfortable place")
        print("   • Sit up straight, relax your shoulders and facial muscles")
        print("   • Close your eyes or focus on the screen")
        print("   • Let go of all thoughts, focus on the present moment")
        print("   • Get ready to follow the breathing rhythm")
    else:
        print("Preparation Tips:")
        print("   • Find a quiet, comfortable place")
        print("   • Sit up straight, relax all your muscles")
        print("   • Close your eyes or focus on the screen")
        print("   • Let go of all thoughts, focus on the present moment")
        print("   • Get ready to follow the breathing rhythm")
        print("   • Stay patient and enjoy the process")
    
    input("\nPress Enter when you're ready to begin...")
    
    # Show session information before countdown
    print("\n" + "=" * 56)
    print("Terminal Zen - Breathing Guide")
    print("Press 'q', 'Esc', or Ctrl+C to exit")
    print(f"Session duration: {session.format_time(session.duration)}")
    print(f"Cycle: Inhale {session.inhale}s, Hold {session.hold1}s, Exhale {session.exhale}s, Hold {session.hold2}s")
    print("-" * 56)
    
    # 10-second countdown with progress bar
    countdown_steps = 100  # 100 steps for smooth progress
    for i in range(countdown_steps):  # Stop at 99, not 100
        progress = i / countdown_steps
        remaining = int(10 * (1 - progress))
        
        # Display countdown progress bar (without brackets)
        bar_width = 40
        # Use round() for proper rounding instead of int() truncation - same as breathing phases
        filled_width = min(round(bar_width * progress), bar_width)
        bar = "█" * filled_width + "░" * (bar_width - filled_width)
        
        print(f"\rStarting in {remaining}s: {bar}", end="", flush=True)
        time.sleep(0.1)
    
    # Explicitly show 100% completion to ensure full bar - clear the line first
    print(f"\rStarting in 0s: {'█' * 40}    ", end="", flush=True)  # Add spaces to clear any leftover chars
    time.sleep(0.3)  # Pause to ensure it's visible
    
    print("\nBegin!\n")


def main():
    """Main CLI entry point."""
    # Check if any arguments were provided
    if len(sys.argv) > 1:
        # Use original argument-based mode
        parser = argparse.ArgumentParser(
            description="Terminal Zen - A terminal-based breathing and meditation guide",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  zen                    # Interactive mode selection
  zen --duration 2m      # 2 minute session
  zen --duration 30s     # 30 second session
  zen --inhale 6 --hold1 3 --exhale 6 --hold2 2  # Custom breathing pattern
  zen --fps 20           # Higher refresh rate
            """
        )
        
        parser.add_argument(
            "--duration", "-d",
            default="60s",
            help="Session duration (e.g., '60s', '2m', '1h') (default: 60s)"
        )
        
        parser.add_argument(
            "--inhale", "-i",
            type=int,
            default=4,
            help="Inhale duration in seconds (default: 4)"
        )
        
        parser.add_argument(
            "--hold1", "-H1",
            type=int,
            default=2,
            help="Hold duration after inhale in seconds (default: 2)"
        )
        
        parser.add_argument(
            "--exhale", "-e",
            type=int,
            default=4,
            help="Exhale duration in seconds (default: 4)"
        )
        
        parser.add_argument(
            "--hold2", "-H2",
            type=int,
            default=2,
            help="Hold duration after exhale in seconds (default: 2)"
        )
        
        parser.add_argument(
            "--fps", "-f",
            type=int,
            default=10,
            help="Progress bar refresh rate (default: 10)"
        )
        
        args = parser.parse_args()
        
        try:
            duration = parse_duration(args.duration)
        except ValueError:
            print("Error: Invalid duration format. Use format like '30s', '2m', or '1h'")
            sys.exit(1)
        
        # Validate timing parameters
        if args.inhale <= 0 or args.hold1 < 0 or args.exhale <= 0 or args.hold2 < 0:
            print("Error: All timing values must be positive (hold can be 0)")
            sys.exit(1)
        
        if args.fps < 1 or args.fps > 60:
            print("Error: FPS must be between 1 and 60")
            sys.exit(1)
        
        # Create and start breathing session
        session = BreathingSession(
            duration=duration,
            inhale=args.inhale,
            hold1=args.hold1,
            exhale=args.exhale,
            hold2=args.hold2,
            fps=args.fps
        )
        
        try:
            session.start()
        except KeyboardInterrupt:
            print("\n\nSession interrupted.")
            sys.exit(0)
    else:
        # Interactive mode
        choice = show_mode_selection()
        config = get_session_config(choice)
        
        # Create breathing session with standard 7-3-7-3 pattern
        session = BreathingSession(
            duration=config["duration"],
            inhale=7,
            hold1=3,
            exhale=7,
            hold2=3,
            fps=10
        )
        
        show_preparation_guide(config["name"], config["duration"], session)
        
        try:
            session.start()
        except KeyboardInterrupt:
            print("\n\nSession interrupted.")
            sys.exit(0)


def parse_duration(duration_str: str) -> int:
    """Parse duration string (e.g., '2m', '30s', '1h') into seconds."""
    duration_str = duration_str.lower().strip()
    
    if duration_str.endswith('s'):
        return int(duration_str[:-1])
    elif duration_str.endswith('m'):
        return int(duration_str[:-1]) * 60
    elif duration_str.endswith('h'):
        return int(duration_str[:-1]) * 3600
    else:
        return int(duration_str)


if __name__ == "__main__":
    main()
