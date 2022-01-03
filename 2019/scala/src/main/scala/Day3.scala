import scala.io.Source

sealed trait Direction
final case class Up(int: Int) extends Direction
final case class Down(int: Int) extends Direction
final case class Left(int: Int) extends Direction
final case class Right(int: Int) extends Direction

object Day3 {
  private val input = Source.fromResource("day3_1.txt").getLines().toList

  def parse(in: String): Direction = {
    in match {
      case s"U$units" => Up(units.toInt)
      case s"D$units" => Down(units.toInt)
      case s"L$units" => Left(units.toInt)
      case s"R$units" => Right(units.toInt)
    }
  }

  def traverse(start: (Int, Int))(path: Seq[Direction]): Seq[(Int, Int)] = {
    val initial = (start, Seq[Seq[(Int, Int)]]())
    path
      .foldLeft(initial) { (acc, nextDirection) =>
        val (current: (Int, Int), previousPaths) = acc
        val paths = nextDirection match {
          case Up(u)    => for (i <- 1 to u) yield (current._1, current._2 + i)
          case Down(u)  => for (i <- 1 to u) yield (current._1, current._2 - i)
          case Left(u)  => for (i <- 1 to u) yield (current._1 - i, current._2)
          case Right(u) => for (i <- 1 to u) yield (current._1 + i, current._2)
        }
        (paths.reverse.head, previousPaths :+ paths)
      }
      ._2
      .flatten
  }

  def main(args: Array[String]): Unit = {
    val firstWire :: secondWire :: Nil =
      input.map(_.split(',').toSeq.map(parse)).map(traverse((0, 0)))
    val intersections = firstWire.toSet & secondWire.toSet
    val minDistance =
      intersections.map(x => Math.abs(x._1) + Math.abs(x._2)).min
    val minSteps = intersections
      .map(is => firstWire.indexOf(is) + secondWire.indexOf(is) + 2)
      .min

    println(minDistance)
    println(minSteps)
  }

}
