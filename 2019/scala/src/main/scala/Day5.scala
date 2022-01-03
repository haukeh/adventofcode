import scala.collection.mutable
import scala.io.Source

object Day5 {

  val outputBuffer = new mutable.ArrayBuffer[Int]()

  final case class Args(noun: Int, verb: Int)

  sealed trait Operation {
    val numArgs: Int
  }

  final case object Mul extends Operation {
    override val numArgs = 3
  }

  final case object Add extends Operation {
    override val numArgs = 3
  }

  final case object In extends Operation {
    override val numArgs = 1
  }

  final case object Out extends Operation {
    override val numArgs = 1
  }

  final case object Halt extends Operation {
    override val numArgs: Int = 0
  }

  final case object JmpT extends Operation {
    override val numArgs: Int = 2
  }

  final case object JmpF extends Operation {
    override val numArgs: Int = 2
  }

  final case object Lt extends Operation {
    override val numArgs: Int = 3
  }

  final case object Eq extends Operation {
    override val numArgs: Int = 3
  }

  final case class Instruction(op: Operation, modes: Seq[Int])

  val globalInput = 5

  def main(args: Array[String]): Unit = {
    val prog: Seq[Int] = Source
      .fromResource("day5_1.txt")
      .getLines()
      .next()
      .trim
      .split(',')
      .map(_.trim)
      .map(_.toInt)
      .toSeq

    val _ = run(mutable.Buffer(prog: _*))

    println(outputBuffer)
  }

  def run(memory: mutable.Buffer[Int]) = calculateOutput(memory)

	@scala.annotation.tailrec
  def calculateOutput(memory: mutable.Buffer[Int], idx: Int = 0): mutable.Buffer[Int] = {
    val (goto, value) = parseInstruction(memory(idx)) match {
      case Instruction(Add, modes)  => add(memory, idx, modes)
      case Instruction(Mul, modes)  => mul(memory, idx, modes)
      case Instruction(In, _)       => readInput(memory, idx)
      case Instruction(Out, modes)  => writeOutput(memory, idx, modes)
      case Instruction(JmpT, modes) => jumpIfTrue(memory, idx, modes)
      case Instruction(JmpF, modes) => jumpIfFalse(memory, idx, modes)
      case Instruction(Lt, modes)   => lessThan(memory, idx, modes)
      case Instruction(Eq, modes)   => equalTo(memory, idx, modes)
      case Instruction(Halt, _)     => return memory
    }
    calculateOutput(memory, if (goto) value else idx + value)
  }

  def parseInstruction(code: Int): Instruction = {
    val seq: Seq[Int] = code.toString.map(_.asDigit).reverse.toList

    def parseModes(op: Operation, params: Seq[Int]) =
      for (i <- 0 until op.numArgs) yield params.lift(i).getOrElse(0)

    val res = seq match {
      case 1 :: 0 :: xs  => Instruction(Add, parseModes(Add, xs))
      case 1 :: xs       => Instruction(Add, parseModes(Add, xs))
      case 2 :: 0 :: xs  => Instruction(Mul, parseModes(Mul, xs))
      case 2 :: xs       => Instruction(Mul, parseModes(Mul, xs))
      case 3 :: _        => Instruction(In, Seq.empty)
      case 4 :: 0 :: xs  => Instruction(Out, parseModes(Out, xs))
      case 4 :: xs       => Instruction(Out, parseModes(Out, xs))
      case 5 :: 0 :: xs  => Instruction(JmpT, parseModes(JmpT, xs))
      case 5 :: xs       => Instruction(JmpT, parseModes(JmpT, xs))
      case 6 :: 0 :: xs  => Instruction(JmpF, parseModes(JmpF, xs))
      case 6 :: xs       => Instruction(JmpF, parseModes(JmpF, xs))
      case 7 :: 0 :: xs  => Instruction(Lt, parseModes(Lt, xs))
      case 7 :: xs       => Instruction(Lt, parseModes(Lt, xs))
      case 8 :: 0 :: xs  => Instruction(Eq, parseModes(Eq, xs))
      case 8 :: xs       => Instruction(Eq, parseModes(Eq, xs))
      case 9 :: 9 :: Nil => Instruction(Halt, Seq.empty)
    }

		res
  }
  def readInput(memory: mutable.Buffer[Int], idx: Int): (Boolean, Int) = {
    val target = memory(idx + 1)
    memory(target) = globalInput
		(false, 2)
  }

  def writeOutput(memory: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
    val outValue = memory(idx + 1)
    val out = if (modes(0) == 1) outValue else memory(outValue)
    outputBuffer += out
		(false, 2)
  }

  def add(input: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
    threeArgOp(input, idx, (a, b) => a + b, modes)
		(false, 4)
  }

  def mul(input: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
    threeArgOp(input, idx, (a, b) => a * b, modes)
		(false, 4)
  }

  def jumpIfTrue(memory: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
    val firstParam = if (modes(0) == 1) memory(idx + 1) else memory(memory(idx + 1))
    val secondParam = if (modes(1) == 1) memory(idx + 2) else memory(memory(idx + 2))
    if (firstParam != 0) (true, secondParam) else (false, 3)
  }

	def jumpIfFalse(memory: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
		val firstParam = if (modes(0) == 1) memory(idx + 1) else memory(memory(idx + 1))
		val secondParam = if (modes(1) == 1) memory(idx + 2) else memory(memory(idx + 2))
		if (firstParam == 0) (true, secondParam) else (false, 3)
	}

	def lessThan(memory: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
		val firstParam = if (modes(0) == 1) memory(idx + 1) else memory(memory(idx + 1))
		val secondParam = if (modes(1) == 1) memory(idx + 2) else memory(memory(idx + 2))
		val thirdParam = memory(idx + 3)
		if (firstParam < secondParam) {
			memory(thirdParam) = 1
		} else {
			memory(thirdParam) = 0
		}
		(false, 4)
	}

	def equalTo(memory: mutable.Buffer[Int], idx: Int, modes: Seq[Int]): (Boolean, Int) = {
		val firstParam = if (modes(0) == 1) memory(idx + 1) else memory(memory(idx + 1))
		val secondParam = if (modes(1) == 1) memory(idx + 2) else memory(memory(idx + 2))
		val thirdParam = memory(idx + 3)
		if (firstParam == secondParam) {
			memory(thirdParam) = 1
		} else {
			memory(thirdParam) = 0
		}
		(false, 4)
	}

  def threeArgOp(input: mutable.Buffer[Int], startIdx: Int, op: (Int, Int) => Int, modes: Seq[Int]): Unit = {
    val valueA = input(startIdx + 1)
    val valueB = input(startIdx + 2)
    val destValue = input(startIdx + 3)
    input(destValue) = op(
      if (modes(0) == 1) valueA else input(valueA),
      if (modes(1) == 1) valueB else input(valueB)
    )
  }
}
