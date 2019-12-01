package day1

import scala.io.Source

object Day1 {

  def main(args: Array[String]): Unit = {
    val p1 = partOne(input)
    println(p1)
    val p2 = partTwo(input)
    println(p2)
  }

  private def input = Source.fromResource("day1_1.txt").getLines().toSeq

  private def partOne(lines: Seq[String]) = {
    lines
      .map(_.toDouble)
      .foldLeft(0) { (acc, value) =>
        acc + calcFuel(value)
      }
  }

  private def calcFuel(value: Double): Int =
    (Math.floor(value / 3.0d) - 2).toInt

  private def partTwo(lines: Seq[String]) = {
    lines
      .map(_.toDouble)
      .flatMap { line =>
        def subcalc(fuel: Int): Seq[Int] = {
          if (fuel <= 0) Nil
          else subcalc(calcFuel(fuel.toDouble)) :+ fuel
        }
        subcalc(calcFuel(line))
      }
      .sum
  }
}
