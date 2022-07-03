import scala.collection.mutable
import scala.io.Source

case class Node(
    name: String,
    weight: Int,
    var parent: Option[Node] = None,
    children: mutable.ListBuffer[Node] = mutable.ListBuffer()
) {
  def totalWeight: Int = weight + children.map(_.totalWeight).sum

  def allChildrenBalanced: Boolean =
    children.map(_.totalWeight).distinct.size == 1

  def findImbalance(diff: Option[Int] = None): Int = {
    if (diff.nonEmpty && allChildrenBalanced) {
      weight - diff.get
    } else {
      val subtrees = children.groupBy(_.totalWeight)
      val unbalancedNode = subtrees.minBy(_._2.size)._2.head

      unbalancedNode.findImbalance(diff.orElse(Option(subtrees.keys.reduce((a, b) => a - b).abs)))
    }
  }
}

object Day7 {

  private val childrenByNode = mutable.Map.empty[String, Seq[String]]
  private val nodesByName = mutable.Map.empty[String, Node]
  def main(args: Array[String]): Unit = {
    val input = Source
      .fromResource("input/d7_ex.txt")
      .getLines()
      .toList

    input.foreach {
      case s"$name ($weight)" =>
        val n = Node(name, weight.toInt)
        nodesByName.put(n.name, n)
      case s"$name ($weight) -> $children" =>
        val n = Node(name, weight.toInt)
        val c = children.trim.split(',').map(_.trim).toSeq
        nodesByName.put(n.name, n)
        childrenByNode.put(n.name, c)
    }

    val leaves = childrenByNode.values.flatten.toSet

    childrenByNode.foreach { case (parent, children) =>
      children.foreach { child =>
        nodesByName(parent).children.addOne(nodesByName(child))
      }
    }

    val root =
      nodesByName.values.filterNot(n => leaves.contains(n.name)).head.name

    println(s"part1: $root")


    val imba = nodesByName(root).findImbalance()

    println(s"part2: $imba")
  }

}
