import numpy as np
import matplotlib.pyplot as plt


def plot_complex_number(z):
    # Extract real and imaginary parts
    real_part = z.real
    imag_part = z.imag

    # Calculate modulus and angle
    modulus = abs(z)
    angle = np.angle(z)

    # Plot the complex number
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection="polar")
    ax.plot([0, angle], [0, modulus], marker="o")
    ax.set_rlabel_position(90)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rmax(modulus + 1)

    # Highlight the circle formed by the modulus
    circle = plt.Circle(
        (0, 0), modulus, color="r", fill=False, linestyle="dashed", linewidth=2
    )
    ax.add_artist(circle)

    # Set labels
    ax.set_rticks([])  # Hide radial ticks
    ax.set_xticks(np.linspace(0, 2 * np.pi, 8, endpoint=False))
    ax.set_xticklabels(
        ["0", "", r"$\frac{\pi}{2}$", "", r"$\pi$", "", r"$\frac{3\pi}{2}$", ""]
    )

    plt.title(f"Complex Number: {z}")
    plt.show()


def plot_complex_number_cartesian(z):
    # Extract real and imaginary parts
    real_part = z.real
    imag_part = z.imag

    # Plot the complex number
    plt.figure(figsize=(8, 8))
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.scatter(real_part, imag_part, color="blue", marker="o")

    # Highlight the circle formed by the modulus
    modulus = abs(z)
    circle = plt.Circle(
        (0, 0), modulus, color="r", fill=False, linestyle="dashed", linewidth=2
    )
    plt.gca().add_patch(circle)

    # Set labels
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.title(f"Complex Number: {z}")

    # Set axis limits
    plt.xlim([-modulus, modulus])
    plt.ylim([-modulus, modulus])

    plt.grid(True)
    plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the sine wave
amplitude = 1.0  # Amplitude of the sine wave
frequency = 1.0  # Frequency of the sine wave in Hz
phase_shift = 0.0  # Phase shift in radians
duration = 2.0  # Duration of the plot in seconds

# Generate time values
t = np.linspace(0, duration, num=1000)

# Generate the sine wave
y = amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)

# Plot the sine wave
plt.figure(figsize=(8, 4))
plt.plot(t, y, label="Sine Wave")

# Set labels and title
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave in Python")

# Display the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
