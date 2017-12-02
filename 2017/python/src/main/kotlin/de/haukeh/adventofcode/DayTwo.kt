package de.haukeh.adventofcode

import java.io.File
import java.util.regex.Pattern

object DayTwo {
    @JvmStatic
    fun main(args: Array<String>) {
        val lines = File("${System.getProperty("user.home")}/Desktop/in.txt").readLines()

        println(checksum(lines) { sumDiffOfMinMax(it) })

        println(checksum(lines) { sumOfEvenlyDivisibles(it) })
    }

    val regex = Pattern.compile("\\s+")

    fun checksum(lines: List<String>, operation: (List<Int>) -> Int): Int {
        return lines.map { it.split(regex).map { Integer.parseInt(it) } }
                .map(operation)
                .sum()
    }

    fun sumDiffOfMinMax(numList: List<Int>): Int = numList.max()!! - numList.min()!!

    fun sumOfEvenlyDivisibles(numList: List<Int>): Int = numList.mapNotNull { first ->
        numList.find { second -> second != first && (first % second == 0) }?.let { Pair(first, it) }
    }.map { it.first / it.second }.first()

}
