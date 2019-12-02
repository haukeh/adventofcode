package day1

import scala.io.Source

object Day2 {

  private var input =
    Source
      .fromResource("day1_1.txt")
      .getLines()
      .toSeq
      .head
      .trim
      .split(',')
      .map(_.toInt)

	def addition(input: Array[Int], i: Int): Unit = {
	}

	def main(args: Array[String]): Unit = {
    input.head match {
      case 1  => ???
      case 2  => ???
      case 99 => ???
    }

  }

}
