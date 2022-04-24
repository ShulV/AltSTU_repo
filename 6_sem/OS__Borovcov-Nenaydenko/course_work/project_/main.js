/* begin view */
/* 
- знает о DOM (удаляет, добавляет, извлекает информацию из DOM элементов) 
- user работает видит view
*/
class View {
    //
    constructor() {
        // this.app = this.getElement('#root');
        // this.processTableContainer = this.getElement('#process-table-container');
        // this.consoleContainer = this.getElement('#console-container');
        // this.processDiagramContainer = this.getElement('#process-diagram-container');
        // this.processQueuesContainer = this.getElement('#process-queues-container');
        //
        
        //
        this.processTable = this.getElement('#process-table-container__table');
        //
        this.addProcessPopup = this.getElement('#add-process-popup');
        this.addProcessOpenBtn = this.getElement('#add-process-popup-open-btn');
        this.addProcessPopupCloseBtn = this.getElement('#add-process-popup-close-btn');
        //this.addProcessForm = this.getElement('#add-process-form');
        this.processNameInput = this.getElement('#process-name-input');
        this.processPriorityInput = this.getElement('#process-priority-input');
        this.processWorkTimeInput = this.getElement('#process-work-time-input');
        this.addProcessBtn = this.getElement('#add-process-btn');
        //
        this.startTimerBtn = this.getElement('#process-diagram-start-timer-btn');
        this.timerTickText = this.getElement('#process-diagram-timer-tick');
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
        const thName = this.createElement('th');
        const thPriority = this.createElement('th');
        const thWorkTime = this.createElement('th');
        const thArrivalTime = this.createElement('th');
        thName.innerHTML = 'Название';
        thPriority.innerHTML = 'Приоритет';
        thWorkTime.innerHTML = 'Время работы';
        thArrivalTime.innerHTML = 'Время прибытия';
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
        const tdName = this.createElement('td');
        const tdPriority = this.createElement('td');
        const tdWorkTime = this.createElement('td');
        const tdArrivalTime = this.createElement('td');
        tdName.innerHTML = process.name;
        tdPriority.innerHTML = process.priority;
        tdWorkTime.innerHTML = process.workTime;
        tdArrivalTime.innerHTML = process.arrivalTime;
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
    openAddProcessPopup() {
        this.addProcessPopup.classList.add('open');
    }
    //
    closeAddProcessPopup() {
        this.addProcessPopup.classList.remove('open');
    }
    //
    bindAddProcess(handler) {
        this.addProcessBtn.addEventListener('click', event => {
          if (event.target.className === 'add-process-form__add-btn') {
            const processName = this.processNameInput.value;
            const processPriority = this.processPriorityInput.value;
            const processWorkTime = this.processWorkTimeInput.value;
    
            handler(processName, processPriority, processWorkTime);
          };
        });
    };
    //
    bindAddProcessPopupOpenBtn(handler) {
        this.addProcessOpenBtn.addEventListener('click', event => {
            if (event.target.className === 'process-table-container__open-popup-btn') {
              this.openAddProcessPopup();
              handler();
            };
          });
    };
    //
    bindAddProcessPopupCloseBtn(handler) {
        this.addProcessPopupCloseBtn.addEventListener('click', event => {
            if (event.target.className === 'add-process-form__close-btn') {
              this.closeAddProcessPopup();
              handler();
            };
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
        this.name = name;
        this.priority = priority;
        this.workTime = workTime;
        this.arrivalTime = arrivalTime;
        this.isCompleted = isCompleted;
    };

};


class Model {
    constructor() {
        this.processList = [];
        this.timerTick = 0;
        this.timerIsStarted = false;
        this.timer = null;
    };
    //
    addProcess(name, priority, workTime) {
        this.processList.push(new Process(name, priority, workTime, this.timerTick));
        this.onProcessListChanged(this.processList);
    };
    //
    startTimer() {
        if (this.timerIsStarted) {
            clearInterval(this.timer);
            this.timerIsStarted = false;
        }
        else {
            this.timer = setInterval(() => {
                this.timerTick++;
                this.onTimerTickChanged(this.timerTick);
            }, 1000);
            this.timerIsStarted = true;
        }
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

      this.view.bindAddProcessPopupOpenBtn(() => {});
      this.view.bindAddProcessPopupCloseBtn(() => {});
      this.view.bindAddProcess(this.handleAddProcess);
      //
      this.view.bindStartTimerBtn(this.handleStartTimer);
      //
      this.model.bindProcessListChanged(this.onProcessListChanged);
      this.model.bindTimerTickChanged(this.onTimerTickChanged);
      
    };
    //
    onProcessListChanged = processList => {
        this.view.displayProcessListTable(processList);
    };
    //
    onTimerTickChanged = timerTick => {
        this.view.displayTimerTick(timerTick);
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
const app = new Controller(new Model(), new View());
/* end anonymous initialize */
