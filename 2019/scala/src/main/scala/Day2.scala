import scala.collection.mutable
import scala.io.Source

object Day2 {

	val initialMemory: Seq[Int] = Source
		.fromResource("day2_1.txt")
		.getLines()
		.next()
		.trim
		.split(',')
		.map(_.toInt)
		.toList

	final case class Args(noun: Int, verb: Int)

	def main(args: Array[String]): Unit = {
		val res: Args = (for {
			noun <- 0 to 99
			verb <- 0 to 99
			output = run(mutable.Buffer(initialMemory: _*), Args(noun, verb))
			if output == 19690720
		} yield Args(noun, verb)).head

		println(s"100 * ${res.noun} + ${res.verb} = ${100 * res.noun + res.verb}")
	}

	def run(memory: mutable.Buffer[Int], arguments: Args): Int = {
		memory(1) = arguments.noun
		memory(2) = arguments.verb
		calculateOutput(memory).head
	}

	@scala.annotation.tailrec
	def calculateOutput(memory: mutable.Buffer[Int], idx: Int = 0, opSize: Int = 4): mutable.Buffer[Int] = {
		memory(idx) match {
			case 1 => add(memory, idx)
			case 2 => mul(memory, idx)
			case 99 => return memory
		}
		calculateOutput(memory, idx + opSize)
	}

	def add(input: mutable.Buffer[Int], idx: Int): Unit =
		threeArgOp(input, idx, (a, b) => a + b)

	def mul(input: mutable.Buffer[Int], idx: Int): Unit =
		threeArgOp(input, idx, (a, b) => a * b)

	def threeArgOp(input: mutable.Buffer[Int], startIdx: Int, op: (Int, Int) => Int): Unit = {
		val indexA = input(startIdx + 1)
		val indexB = input(startIdx + 2)
		val destIndex = input(startIdx + 3)
		input(destIndex) = op(input(indexA), input(indexB))
	}
}
