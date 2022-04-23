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
        this.processTable = this.getElement('#process-table');

        this.processNameInput = this.getElement('#process-name-input');
        this.processPriorityInput = this.getElement('#process-priority-input');
        this.processWorkTimeInput = this.getElement('#process-work-time-input');
        this.addProcessBtn = this.getElement('#add-process-btn');
        
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
};
/* end view */

/* begin model */
/* 
В модели только храним данные и производим манипуляции над ними
- не знает о DOM
- user не работает с model напрямую
*/
class Process {
    constructor(name, priority, workTime, arrivalTime=0, isCompleted=false) {
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
    };
    //
    addProcess(name, priority, workTime) {
        this.processList.push(new Process(name, priority, workTime));
        this.onProcessListChanged(this.processList);
    };
    //
    bindProcessListChanged(callback) {
        this.onProcessListChanged = callback;
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

      this.view.bindAddProcess(this.handleAddProcess);
      this.model.bindProcessListChanged(this.onProcessListChanged);
    };
    //
    onProcessListChanged = processList => {
        this.view.displayProcessListTable(processList);
    };
    //
    handleAddProcess = (name, workTime, priority) => {
        this.model.addProcess(name, workTime, priority);
    };
    //

};
/* end controller */

/* begin anonymous initialize */
const app = new Controller(new Model(), new View());
/* end anonymous initialize */