object Day4 {

  def isValid(num: Int): Boolean = {
    val digits = num.toString.map(_.asDigit)

    for (i <- 0 to 4) {
      if (digits(i) > digits(i + 1)) {
        return false
      }
    }

    var validGroups = 0
    var sameDigitGroups = 0
    for (i <- 0 to 4) {
      if (digits(i) == digits(i + 1)) {
        sameDigitGroups += 1
        if (sameDigitGroups == 1) {
					validGroups += 1
				} else if (sameDigitGroups == 2) {
					validGroups -= 1
        }
      } else {
        sameDigitGroups = 0
      }
    }

    validGroups > 0
  }

  def main(args: Array[String]): Unit = {
    val combinations = for (num <- 235741 to 706948 if isValid(num)) yield num

    println(combinations)
    println(combinations.length)
  }

}
