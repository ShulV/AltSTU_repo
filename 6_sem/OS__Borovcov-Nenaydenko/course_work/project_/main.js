const MAX_PRIORITY = 8;
const CORE_NUM = 4;
const RULER_STEP = 5;
const ONE_TICK_LENGTH = 20;
const TICK_TIME_IN_SECONDS = 1;

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
        this.processDiagramCoreLines = [];
        this.diagramRuler = null;
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
        let processQueueText = '';
        for(let i=0; i<processQueue.length; i++) {
            processQueueText += processQueue[i].id + ', ';
        }
        processQueueText = processQueueText.slice(0, -2);
        tdQueue.innerHTML = processQueueText;
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
    displayDiagramRuler(timerTick) {
        let rulerStep = RULER_STEP;
        let labelNum = Math.ceil(timerTick/rulerStep);
        for(let i=0; i<labelNum; i++) {
            let label = this.createElement('div', 'process-diagram-container__diagram-ruler-segment');
            label.textContent = i * rulerStep;
            label.style.width = (ONE_TICK_LENGTH*RULER_STEP)+'px';
            this.diagramRuler.appendChild(label);
        }
    };
    //
    displayDiagram(processor, timerTick) {
        if (this.processDiagram.firstChild) {
            //clean inside exisiting containers (lines)
            for(let i=0; i<processor.coreNum; i++){
                this.processDiagramCoreLines[i].innerHTML = '';
                this.diagramRuler.innerHTML = '';
            }
        }
        else {
            //create core containers (lines)
            for(let i=0; i<processor.coreNum; i++) {
                let coreLine = this.createElement('div', 'process-diagram-container__diagram-core-line');
                this.processDiagramCoreLines.push(coreLine);
                this.processDiagram.appendChild(coreLine);
            }
            let rulerLine = this.createElement('div', 'process-diagram-container__diagram-ruler');
                this.diagramRuler = rulerLine;
                this.processDiagram.appendChild(rulerLine);            
        }
        //fill them
        //go all lines
        for(let i=0; i<processor.coreNum; i++) {
            for(let j=0; j<processor.completedProcesses[i].length; j++) {
                let coreLineProcess = Object();
                if (processor.completedProcesses[i][j].id == 0) {
                    coreLineProcess = this.createElement('div', 'process-diagram-container__diagram-empty-process');
                }
                else {
                    coreLineProcess = this.createElement('div', 'process-diagram-container__diagram-completed-process');
                    coreLineProcess.innerHTML = processor.completedProcesses[i][j].id;
                    let tickWorked = processor.completedProcesses[i][j].workTime - processor.completedProcesses[i][j].remainingWorkTime;
                    coreLineProcess.style.width = (ONE_TICK_LENGTH*tickWorked)+'px';
                }
                this.processDiagramCoreLines[i].appendChild(coreLineProcess);
            }
            if (processor.runningProcesses[i]) {
                let coreLineProcess = Object();
                if (processor.runningProcesses[i].id == 0) {
                    coreLineProcess = this.createElement('div', 'process-diagram-container__diagram-empty-process');
                }
                else {
                    coreLineProcess = this.createElement('div', 'process-diagram-container__diagram-running-process');
                    coreLineProcess.innerHTML = processor.runningProcesses[i].id;
                    let tickWorked = processor.runningProcesses[i].workTime - processor.runningProcesses[i].remainingWorkTime;
                    coreLineProcess.style.width = (ONE_TICK_LENGTH*tickWorked)+'px';
                }
                this.processDiagramCoreLines[i].appendChild(coreLineProcess);
            }            
        }
        this.displayDiagramRuler(timerTick);
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
            const processPriority = Number(this.processPriorityInput.value);
            const processWorkTime = Number(this.processWorkTimeInput.value);
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
        this.remainingWorkTime = workTime;
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
        this.emptyProcess = new Process('empty', 0, 1, 0);
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
        this.addProcessInQueue(newProcess);
    };
    //
    addProcessesToRun() {
        // определение количества свободных (готовых принять новый процесс на выполнение) ядер
        let necessaryProcessesNum = 0;
        for(let j=0; j<this.processor.coreNum; j++) {
            if (this.processor.runningProcesses[j] == null) {
                necessaryProcessesNum++;
            }
        }
        console.log(`количество необходимых процессов для заполнения = ${necessaryProcessesNum}`);
        // заполнение массива необходимым количеством процессов из очереди
        let necessaryProcesses = [];
        for(let i=MAX_PRIORITY-1; i>0; i--) {
            if (this.processQueuesByPriority[i].length>0) {
                while (this.processQueuesByPriority[i].length > 0) {
                    if (necessaryProcesses.length == necessaryProcessesNum) {
                        this.sendProcessesToProcessor(necessaryProcesses);
                        return;
                    }
                    necessaryProcesses.push(this.processQueuesByPriority[i].shift());
                    //событие изменение числа событий в очереди (в обработчике перерисовка очередей процессов)
                    this.onProcessQueuesChanged(this.processQueuesByPriority);
                    //если из очереди забрали необходимое количество процессов, отправляем их в процессор и выходим
                    console.log(`\nthis.processQueuesByPriority[${i}].length ${this.processQueuesByPriority[i].length}`)
                    console.log(`necessaryProcesses.length ${necessaryProcesses.length}\n---\n`);

                    
                }
            }
        }
        if (necessaryProcesses.length == necessaryProcessesNum) {
            this.sendProcessesToProcessor(necessaryProcesses);
            return;
        }
        console.log(`очередь: ${this.processQueuesByPriority[0]}`)
        console.log(`процессов из очереди взято ${necessaryProcesses.length}, дозаполняем пустыми процессами`);
        // дозаполнение массива пустыми процессами, если процессов в очереди не осталось
        while (necessaryProcesses.length != necessaryProcessesNum) {
            // копируем объект дефолтного пустого процесса
            necessaryProcesses.push(Object.assign({}, this.processor.emptyProcess));
        }
        //отправляем процессы в процессор
        this.sendProcessesToProcessor(necessaryProcesses);
        return;
    };
    // положить процессы в ядра процессора для выполнения
    sendProcessesToProcessor(processes) {
        console.log('процессы переданные в функц')
        processes.forEach((item) => {
            console.log(item.id)
        })
        for(let i=0; i<this.processor.coreNum; i++) {
            if (this.processor.runningProcesses[i] == null) {
                this.processor.runningProcesses[i] = processes.shift();
                console.log(`this.processor.runningProcesses[${i}] = ${this.processor.runningProcesses[i].id}`)
            }
        }
        console.log(`положили процессы в ядра; переменная processes.length = ${processes.length} (нужно 0)`);
        console.log('-------------------------------------------------------------------------')

    };
    //
    startTimer() {
        if (this.timerIsStarted) {
            clearInterval(this.timer);
            this.timerIsStarted = false;
        }
        else {
            this.timer = setInterval(() => {
                console.log('\nФункция таймера')
                //добавление процессов в ядра процессора на выполнение (если очередь пуста - пустыми процессами-заглушками)
                this.addProcessesToRun();
                //
                this.runProcessForTick();
                //событие вызывает перерисовку диаграммы (линии с процессами ядер + линейка)
                this.onProcessorPropsChanged(this.processor, this.timerTick);
                this.timerTick++;
                //событие вызывает перерисовку показателя таймера
                this.onTimerTickChanged(this.timerTick);
            }, 1000 * TICK_TIME_IN_SECONDS);
            this.timerIsStarted = true;
        };
    };
    //
    runProcessForTick() {
        // for(let i=0; i<this.processor.coreNum; i++) {
        //     if ( this.processor.runningProcesses[i] == null) {
        //         continue;
        //     }
        // }
        for(let i=0; i<this.processor.coreNum; i++) {
            this.processor.runningProcesses[i].remainingWorkTime--;

            if (this.processor.runningProcesses[i].remainingWorkTime == 0) {
                this.processor.completedProcesses[i].push(this.processor.runningProcesses[i]);
                this.processor.runningProcesses[i] = null;
            }         
        }
    };
    //
    addProcessInQueue(process) {
        this.processQueuesByPriority[process.priority].push(process);
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
    onProcessorPropsChanged = (processor, timerTick) => {
        this.view.displayDiagram(processor, timerTick);
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
