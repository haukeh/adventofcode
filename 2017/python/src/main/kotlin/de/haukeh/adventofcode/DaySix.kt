package de.haukeh.adventofcode

import java.util.regex.Pattern


object DaySix {

    val input = "4\t10\t4\t1\t8\t4\t9\t14\t5\t1\t14\t15\t0\t15\t3\t5"

    val regex = Pattern.compile("\\s+")


    @JvmStatic
    fun main(args: Array<String>) {
        val memBank = input.split(regex).map { Integer.parseInt(it) }.toTypedArray()
        val snapshots = mutableListOf<String>()
        var loops = 0

        while (!snapshots.contains(memBank.joinToString { it.toString() })) {
            snapshots.add(memBank.joinToString { it.toString() })
            val max = memBank.max() ?: throw IllegalArgumentException()
            var idx = memBank.indexOfFirst { it == max }
            var num = memBank[idx]
            memBank[idx] = 0

            while (num != 0) {
                memBank[(idx + 1) % memBank.size] += 1
                num--
                idx++
            }

            loops++
        }

        println("operations: ${loops}")

        println("loop size: ${snapshots.size - snapshots.indexOf(memBank.joinToString { it.toString() })}")
    }

}
