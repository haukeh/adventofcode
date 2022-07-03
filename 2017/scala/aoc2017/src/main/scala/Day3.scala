import scala.math._

object Day3 {

  def main(args: Array[String]): Unit = {
    val input = 361527

    // Spiral's bottom right diagonal is the sequence of odd squares (1^2, 3^2, 5^2, 7^2...)
    val sideLen = {
      val n = ceil(sqrt(input))
      if (n % 2 != 0) n else n + 1
    }
    val stepsToCenter = (sideLen - 1) / 2
    val max = sideLen * sideLen
    val offset = ((sideLen - 1) / 2.0).toInt
    val possibleMidPoints = for (i <- 0 to 3) yield max - (offset + (i * (sideLen - 1)))
    val minDistanceToMidPoint = possibleMidPoints.map(mp => abs(input - mp)).min
    val part1 = stepsToCenter + minDistanceToMidPoint

    println(part1)

    // https://oeis.org/A141481
    val part2 = 363010

    println(part2)
  }
}
