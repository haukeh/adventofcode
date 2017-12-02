package de.haukeh.adventofcode

import org.junit.Assert.assertEquals
import org.junit.Test

class DayTwoTest {

    @Test
    fun testPart1() {
        val input = listOf("5 1 9 5", "7 5 3", "2 4 6 8")

        assertEquals(DayTwo.checksum(input, { DayTwo.sumDiffOfMinMax(it) }), 18)
    }

    @Test
    fun testPart2() {
        val input = listOf("5 9 2 8", "9 4 7 3", "3 8 6 5")

        assertEquals(DayTwo.checksum(input) { DayTwo.sumOfEvenlyDivisibles(it) }, 9)
    }
}
