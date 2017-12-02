package de.hauke.adventofcode

import java.io.File

object DayOne {
    @JvmStatic
    fun main(args: Array<String>) {
        val inputString = File("${System.getProperty("user.home")}/Desktop/in.txt").readText()

        println("Part1: ${solveCaptcha(inputString, 1)}")
        println("Part2: ${solveCaptcha(inputString, inputString.length / 2)}")
    }

    fun solveCaptcha(input: String, offset: Int): Int {
        return input.filterIndexed { idx, e -> (input[(idx + offset) % input.length] == e) }
                .map { it - '0' }
                .sum()
    }
}
