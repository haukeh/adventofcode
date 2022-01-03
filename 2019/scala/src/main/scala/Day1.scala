import scala.io.Source

object Day1 {

  def main(args: Array[String]): Unit = {
    val p1 = partOne(input)
    println(p1)
    val p2 = partTwo(input)
    println(p2)
  }

  private def input = Source.fromResource("day1_1.txt").getLines().toSeq

	private def calcFuel(value: Int): Int = value / 3 - 2

  private def partOne(lines: Seq[String]) =
    lines
      .map(_.toInt)
      .map(calcFuel)
      .sum

  private def partTwo(lines: Seq[String]) =
    lines
      .map(_.toInt)
      .flatMap { line =>
        def subcalc(fuel: Int): Seq[Int] =
          if (fuel <= 0) Nil else subcalc(calcFuel(fuel)) :+ fuel
        subcalc(calcFuel(line))
      }
      .sum
}
