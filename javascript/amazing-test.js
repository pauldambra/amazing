var seedrandom = require('seedrandom')
var assert = require('assert')
var amazing = require('./amazing')

describe('Amazing', function() {

  it('works for large mazes', function() {
    seedrandom(0, { global: true })
    var expected = "Amazing - Copyright by Creative Computing, Morristown, NJ\n" +
      "+  +--+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +
      "|              |           |        |        | \n" +
      "+--+  +--+--+  +  +  +  +  +  +--+  +  +--+  +\n" +
      "|  |        |     |  |  |     |  |     |     | \n" +
      "+  +--+  +  +--+--+  +--+--+--+  +  +--+  +--+\n" +
      "|  |     |  |     |     |     |     |     |  | \n" +
      "+  +  +--+  +  +  +--+  +  +  +--+--+--+  +  +\n" +
      "|  |     |  |  |  |     |  |     |     |     | \n" +
      "+  +--+  +  +  +  +  +--+  +--+  +  +  +--+--+\n" +
      "|  |     |  |  |  |  |  |     |  |  |        | \n" +
      "+  +  +--+  +  +  +  +  +  +  +  +  +--+--+  +\n" +
      "|     |     |  |     |     |  |     |     |  | \n" +
      "+--+--+  +--+--+--+--+  +--+--+--+--+  +  +  +\n" +
      "|        |           |  |           |  |     | \n" +
      "+--+  +--+  +--+--+  +  +  +--+--+  +--+--+  +\n" +
      "|     |     |     |     |  |     |     |     | \n" +
      "+  +--+--+--+  +  +--+  +  +--+  +  +  +  +--+\n" +
      "|              |     |  |     |  |  |     |  | \n" +
      "+--+--+--+  +  +--+  +--+  +  +  +  +--+--+  +\n" +
      "|        |  |     |     |  |     |     |     | \n" +
      "+  +--+  +  +--+--+  +  +--+--+  +  +  +  +--+\n" +
      "|     |  |  |        |        |  |  |  |     | \n" +
      "+--+  +  +  +  +--+--+--+--+  +  +  +  +--+  +\n" +
      "|     |  |  |     |        |     |  |     |  | \n" +
      "+  +--+  +--+--+  +  +  +--+  +--+--+--+  +  +\n" +
      "|  |     |        |  |  |        |        |  | \n" +
      "+  +  +--+  +--+--+  +--+  +--+  +  +--+--+  +\n" +
      "|  |        |     |     |  |  |  |        |  | \n" +
      "+  +--+--+--+  +--+--+  +  +  +  +  +--+  +  +\n" +
      "|  |        |     |     |  |     |     |  |  | \n" +
      "+  +--+--+  +  +  +  +--+  +  +--+--+  +--+  +\n" +
      "|           |  |  |        |  |     |        | \n" +
      "+  +  +--+--+  +  +--+--+--+  +  +  +--+--+--+\n" +
      "|  |  |  |     |  |        |     |     |     | \n" +
      "+  +  +  +  +  +  +--+  +--+--+--+  +  +  +  +\n" +
      "|  |     |  |  |     |  |        |  |  |  |  | \n" +
      "+  +--+--+  +  +--+  +  +  +--+  +--+  +--+  +\n" +
      "|           |     |        |  |     |     |  | \n" +
      "+  +--+--+--+--+--+--+--+--+  +  +  +--+  +  +\n" +
      "|                             |  |     |     | \n" +
      "+--+--+--+--+--+--+--+--+--+--+  +--+--+--+--+\n"

    assert.equal(amazing.doit(15, 20), expected)
  })

  it('works for small mazes', function() {
    seedrandom(101, { global: true })
    var expected = "Amazing - Copyright by Creative Computing, Morristown, NJ\n" +
      "+--+--+  +--+\n" +
      "|           | \n" +
      "+  +  +--+  +\n" +
      "|  |     |  | \n" +
      "+  +--+  +  +\n" +
      "|  |     |  | \n" +
      "+--+  +--+  +\n" +
      "|     |  |  | \n" +
      "+  +--+  +  +\n" +
      "|        |  | \n" +
      "+--+--+--+  +\n"

    assert.equal(amazing.doit(4, 5), expected)
  })

})

