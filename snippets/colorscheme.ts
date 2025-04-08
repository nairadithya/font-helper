// Stolen completely from https://supergeekery.com/blog/create-mathematically-generated-css-color-schemes-with-oklch

/**
 * Creates a pseudo-random float in the range [0, 1) using Math.sin
 * of a seed, ensuring a stable output for each unique integer seed.
 */
document.addEventListener('astro:page-load', () => {
    function seededRandom(daySeed: number): number {
        const x: number = Math.sin(daySeed) * 10000
        return x - Math.floor(x)
    }

    /**
     * Returns a pseudo-random hue for the current day, but remains the same
     * for that day. The hue resets the next day.
     */
    function getDailyHueSeeded(): number {
        const now: Date = new Date()
        const startOfYear: Date = new Date(now.getFullYear(), 0, 1)

        // Number of days since Jan 1
        const dayOfYear: number = Math.floor(
            (now.getTime() - startOfYear.getTime()) / (24 * 60 * 60 * 1000)
        )
        // Convert that to a random float
        const randomValue: number = seededRandom(dayOfYear + 1)

        // Scale up to 360 deg
        return Math.floor(randomValue * 360)
    }

    const hueSeeded: number = getDailyHueSeeded()
    document.documentElement.style.setProperty('--hue', `${hueSeeded}deg`)
})

function seededRandom(daySeed: number): number {
    const x: number = Math.sin(daySeed) * 10000
    return x - Math.floor(x)
}

/**
 * Returns a pseudo-random hue for the current day, but remains the same
 * for that day. The hue resets the next day.
 */
function getDailyHueSeeded(): number {
    const now: Date = new Date()
    const startOfYear: Date = new Date(now.getFullYear(), 0, 1)

    // Number of days since Jan 1
    const dayOfYear: number = Math.floor(
        (now.getTime() - startOfYear.getTime()) / (24 * 60 * 60 * 1000)
    )
    // Convert that to a random float
    const randomValue: number = seededRandom(dayOfYear)

    // Scale up to 360 deg
    return Math.floor(randomValue * 360)
}

const hueSeeded: number = getDailyHueSeeded()
document.documentElement.style.setProperty('--hue', `${hueSeeded}deg`)
