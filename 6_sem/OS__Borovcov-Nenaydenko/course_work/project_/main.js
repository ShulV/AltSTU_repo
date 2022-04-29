const MAX_PRIORITY = 256;
const CORE_NUM = 4;
/* begin view */
/* 
- знает о DOM (удаляет, добавляет, извлекает информацию из DOM элементов) 
- user работает видит view
*/
class View {
    //
    constructor() {       
        //process-table-container
        this.processTable = this.getElement('#process-table');
        this.addingProcessPopup = this.getElement('#adding-process-popup');
        this.addingProcessOpenBtn = this.getElement('#adding-process-popup-open-btn');
        //
        this.addingProcessPopupCloseBtn = this.getElement('#adding-process-popup-close-btn');
        this.processNameInput = this.getElement('#process-name-input');
        this.processPriorityInput = this.getElement('#process-priority-input');
        this.processWorkTimeInput = this.getElement('#process-work-time-input');
        this.addingProcessBtn = this.getElement('#adding-process-btn');
        //
        this.processDiagram = this.getElement('#process-diagram');
        this.startTimerBtn = this.getElement('#process-diagram-start-timer-btn');
        this.timerTickText = this.getElement('#process-diagram-timer-tick');
        //
        this.processQueueTable = this.getElement('#process-queues-table');
        //
    };
    //
    createElement(tag, className) {
        const element = document.createElement(tag);
    
        if (className) element.classList.add(className);
    
        return element;
    };
    //
    getElement(selector) {
        const element = document.querySelector(selector);
    
        return element;
    };
    //
    createProcessTableHeaders() {
        const thead = this.createElement('thead');
        const trHeaders = this.createElement('tr');
        const thId = this.createElement('th');
        const thName = this.createElement('th');
        const thPriority = this.createElement('th');
        const thWorkTime = this.createElement('th');
        const thArrivalTime = this.createElement('th');
        thId.innerHTML = 'Id';
        thName.innerHTML = 'Название';
        thPriority.innerHTML = 'Приоритет';
        thWorkTime.innerHTML = 'Время работы';
        thArrivalTime.innerHTML = 'Время прибытия';
        trHeaders.appendChild(thId);
        trHeaders.appendChild(thName);
        trHeaders.appendChild(thPriority);
        trHeaders.appendChild(thWorkTime);
        trHeaders.appendChild(thArrivalTime);
        thead.appendChild(trHeaders);
        this.processTable.appendChild(thead);
    };
    //
    createProcessRowInTable(tbody, process) {
        const tr = this.createElement('tr');
        const tdId = this.createElement('td');
        const tdName = this.createElement('td');
        const tdPriority = this.createElement('td');
        const tdWorkTime = this.createElement('td');
        const tdArrivalTime = this.createElement('td');
        tdId.innerHTML = process.id;
        tdName.innerHTML = process.name;
        tdPriority.innerHTML = process.priority;
        tdWorkTime.innerHTML = process.workTime;
        tdArrivalTime.innerHTML = process.arrivalTime;
        tr.appendChild(tdId);
        tr.appendChild(tdName);
        tr.appendChild(tdPriority);
        tr.appendChild(tdWorkTime);
        tr.appendChild(tdArrivalTime);
        tbody.appendChild(tr);
    };
    //
    displayProcessListTable(processList) {
        //clear the table
        this.processTable.innerHTML = '';
        //
        this.createProcessTableHeaders();
        const tbody = this.createElement('tbody');
        processList.forEach(process => {
            this.createProcessRowInTable(tbody, process);
        });
        this.processTable.appendChild(tbody);
    }
    //
    displayTimerTick(timerTick) {
        this.timerTickText.textContent = timerTick;
    }
    //
    createProcessQueuesTableHeaders() {
        const thead = this.createElement('thead');
        const tr = this.createElement('tr');
        const thPriority = this.createElement('th');
        const thQueue = this.createElement('th');
        thPriority.innerHTML = 'Приоритет';
        thQueue.innerHTML = 'Очередь';
        tr.appendChild(thPriority);
        tr.appendChild(thQueue);
        thead.appendChild(tr);
        this.processQueueTable.appendChild(thead);
    };
    //
    createQueueWithPriorityRow(tbody, priority, processQueue) {
        const tr = this.createElement('tr');
        const tdPriority = this.createElement('td');
        tdPriority.innerHTML = priority;
        tr.appendChild(tdPriority);
        const tdQueue = this.createElement('td');
        tdQueue.innerHTML = processQueue;
        tr.appendChild(tdQueue);
        tbody.appendChild(tr);
    }
    //
    displayProcessQueues(processQueues) {
        //clear the table
        this.processQueueTable.innerHTML = '';
        this.createProcessQueuesTableHeaders();
        const tbody = this.createElement('tbody');
        for(let i=0; i<processQueues.length; i++) {
            if (processQueues[i] != '') {
                this.createQueueWithPriorityRow(tbody, i, processQueues[i]);
            }
        }
        this.processQueueTable.appendChild(tbody);
    };
    //
    displayDiagram(coreNum) {
        console.log('DISPLAY')
        if (this.processDiagram.firstChild) {
            console.log(this.processDiagram.firstChild)
        }
        else {
            for(let i=0; i<coreNum; i++) {
                console.log('создали' + i)
                let coreLine = this.createElement('div', 'process-diagram-container__diagram-core-line');
                this.processDiagram.appendChild(coreLine);
            }
        }
    };
    //
    openAddingProcessPopup() {
        this.addingProcessPopup.classList.add('open');
    };
    //
    closeAddingProcessPopup() {
        this.addingProcessPopup.classList.remove('open');
    };
    //
    bindAddProcess(handler) {
        this.addingProcessBtn.addEventListener('click', event => {
          if (event.target.className === 'adding-process-form__add-btn') {
            const processName = this.processNameInput.value;
            const processPriority = this.processPriorityInput.value;
            const processWorkTime = this.processWorkTimeInput.value;
            if (processName == '' || processPriority == '' || processWorkTime == '') {
                //TODO сделать валидацию формы
                console.log('Данные не введены');
            }
            else {
                handler(processName, processPriority, processWorkTime);
            }
            
          }
        });
    };
    //
    bindAddingProcessPopupOpenBtn(handler) {
        this.addingProcessOpenBtn.addEventListener('click', event => {
            if (event.target.className === 'process-table-container__open-popup-btn') {
              this.openAddingProcessPopup();
              handler();
            };
          });
    };
    //
    bindAddingProcessPopupCloseBtn(handler) {
        this.addingProcessPopupCloseBtn.addEventListener('click', event => {
            if (event.target.className === 'adding-process-form__close-btn') {
              this.closeAddingProcessPopup();
              handler();
            }
        });
    };
    //
    bindStartTimerBtn(handler) {
        this.startTimerBtn.addEventListener('click', event => {
            if (event.target.classList.contains('process-diagram-container__control-start-timer-btn')) {
              this.startTimerBtn.classList.toggle('started');
              handler();
            };
          });
    };
    //
};
/* end view */

/* begin model */
/* 
В модели только храним данные и производим манипуляции над ними
- не знает о DOM
- user не работает с model напрямую
*/
class Process {
    constructor(name, priority, workTime, arrivalTime, isCompleted=false) {
        this.id = Process.processCounter++;
        this.name = name;
        this.priority = priority;
        this.workTime = workTime;
        this.arrivalTime = arrivalTime;
        this.isCompleted = isCompleted;
    };
};

class Processor {
    constructor(coreNum) {
        this.coreNum = coreNum;
        this.runningProcesses = [];
        this.completedProcesses = [];
        for(let i=0; i<coreNum; i++) {
            this.runningProcesses.push(null);
            this.completedProcesses.push([]);
        }
    };
};

class Model {
    constructor() {
        this.processList = [];
        this.timerTick = 0;
        this.timerIsStarted = false;
        this.timer = null;
        this.processQueuesByPriority = [];
        for(let i=0; i<MAX_PRIORITY; i++) {
            this.processQueuesByPriority.push([]);
        }
        this.processor = new Processor(CORE_NUM);
    };
    //
    addProcess(name, priority, workTime) {
        const newProcess = new Process(name, priority, workTime, this.timerTick);
        this.processList.push(newProcess);
        this.onProcessListChanged(this.processList);
        this.addProcessInQueue(newProcess.priority, newProcess.id);
    };
    //
    addProcessesToRun() {
        for(let i=MAX_PRIORITY-1; i>0; i--) {
            if (this.processQueuesByPriority[i].length>0) {
                // console.log(`зашли в очередь ${i}.`);
                for(let j=0; j<this.processor.coreNum; j++) {
                    // console.log(`проверяем ядро ${j}.`);
                    if (this.processor.runningProcesses[j] == null) {
                        let process = this.processQueuesByPriority[i].shift();
                        this.processor.runningProcesses[j] = process;
                        // console.log(`в ядро ${j} процессора положили процесс ${process}.`)
                        this.onProcessQueuesChanged(this.processQueuesByPriority);
                    }
                    else {
                        continue;
                    }
                }
            }
        }
    };
    //
    startTimer() {
        if (this.timerIsStarted) {
            clearInterval(this.timer);
            this.timerIsStarted = false;
        }
        else {
            this.timer = setInterval(() => {
                this.onProcessorPropsChanged(this.processor.coreNum);
                this.addProcessesToRun();
                this.timerTick++;
                this.onTimerTickChanged(this.timerTick);
            }, 1000);
            this.timerIsStarted = true;
        };
    };
    //
    addProcessInQueue(processPriority, processId) {
        this.processQueuesByPriority[processPriority].push(processId);
        this.onProcessQueuesChanged(this.processQueuesByPriority);
    };
    //-----------------------------------------------------------------------------------
    bindProcessQueuesChanged(callback) {
        this.onProcessQueuesChanged = callback;
    }
    //
    bindProcessListChanged(callback) {
        this.onProcessListChanged = callback;
    };
    //
    bindTimerTickChanged(callback) {
        this.onTimerTickChanged = callback;
    };
    //
    bindProcessorPropsChanged(callback) {
        this.onProcessorPropsChanged = callback;
    }
    //
  };
/* end model */

/* begin controller */
/* 
- не знает о DOM
- user что-то меняет через controller
*/
class Controller {
    constructor(model, view) {
      this.model = model
      this.view = view
      //
      this.view.bindAddingProcessPopupOpenBtn(() => {});
      this.view.bindAddingProcessPopupCloseBtn(() => {});
      this.view.bindAddProcess(this.handleAddProcess);
      //
      this.view.bindStartTimerBtn(this.handleStartTimer);
      //
      this.model.bindProcessListChanged(this.onProcessListChanged);
      //
      this.model.bindProcessQueuesChanged(this.onProcessQueuesChanged);
      //
      this.model.bindTimerTickChanged(this.onTimerTickChanged);
      this.model.bindProcessorPropsChanged(this.onProcessorPropsChanged);
      
    };
    //
    onProcessListChanged = processList => {
        this.view.displayProcessListTable(processList);
    };
    //
    onProcessQueuesChanged = processQueues => {
        this.view.displayProcessQueues(processQueues);
    }
    //
    onTimerTickChanged = timerTick => {
        this.view.displayTimerTick(timerTick);
    };
    //
    onProcessorPropsChanged = (coreNum) => {
        this.view.displayDiagram(coreNum);
    };
    //
    handleAddProcess = (name, workTime, priority) => {
        this.model.addProcess(name, workTime, priority);
    };
    //
    handleStartTimer = () => {
        this.model.startTimer();
    }
    //

};
/* end controller */

/* begin anonymous initialize */
Process.processCounter = 0;
const app = new Controller(new Model(), new View());
/* end anonymous initialize */
