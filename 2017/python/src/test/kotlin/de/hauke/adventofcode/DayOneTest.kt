package de.hauke.adventofcode

import org.junit.Assert.assertEquals
import org.junit.Test

class DayOneTest {

    @Test
    fun test1() {
        assertEquals(DayOne.solveCaptcha("91212129", 1), 9)
    }

    @Test
    fun test2() {
        assertEquals(DayOne.solveCaptcha("1122", 1), 3)
    }

    @Test
    fun test3() {
        assertEquals(DayOne.solveCaptcha("1111", 1), 4)
    }

    @Test
    fun test4() {
        assertEquals(DayOne.solveCaptcha("1234", 1), 0)
    }
}
