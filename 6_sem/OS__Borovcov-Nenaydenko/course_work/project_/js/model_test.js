const test_app = new Controller(new Model(), new View());

describe("model.addProcess('processName', 1, 4)", function() {
  app.model.addProcess('processName', 1, 4);
    it("processList.length == 1", function() {
      
      assert.equal(test_app.model.processList.length, 1);
    });

  });

//   addProcess('processName', 1, 4) {
//     const newProcess = new Process(name, priority, workTime, this.timerTick);
//     this.processList.push(newProcess);
//     this.onProcessListChanged(this.processList);
//     this.addProcessInQueue(newProcess);
// };