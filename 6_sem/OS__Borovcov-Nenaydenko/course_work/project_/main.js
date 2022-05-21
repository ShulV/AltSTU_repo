//push() добавить в конец
//unshift() добавить в начало
//pop() удалить из конца
//shift() удалить из начала




const MAX_PRIORITY = 255;
const CORE_NUM = 4;
const RULER_STEP = 5;
const ONE_TICK_LENGTH = 40;
const TICK_TIME_IN_SECONDS = 1;
const AUTO_ID_NUM = -1;

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
        this.processArrivalTimeInput = this.getElement('#process-arrival-time-input');
        this.addingProcessBtn = this.getElement('#adding-process-btn');
        //
        this.processDiagram = this.getElement('#process-diagram');
        this.processDiagramCoreLines = [];
        this.diagramRuler = null;
        this.startTimerBtn = this.getElement('#process-diagram-start-timer-btn');
        this.timerTickTextBlock = this.getElement('#process-diagram-timer-tick');
        //
        this.processQueueTable = this.getElement('#process-queues-table');
        //
        this.consoleContainerEntries = this.getElement('#console-container__entries');
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
        this.timerTickTextBlock.textContent = timerTick;
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
        console.log('ЛИНЕЙКА')
        let labelNum = Math.ceil((timerTick + 1)/RULER_STEP);
        console.log(`labelNum = ${labelNum}`)
        for(let i=0; i<labelNum; i++) {
            let label = this.createElement('div', 'process-diagram-container__diagram-ruler-segment');
            label.textContent = i * RULER_STEP + ' тиков';
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
                    coreLineProcess.innerHTML = `p${processor.completedProcesses[i][j].id}(${processor.completedProcesses[i][j].priority})`;
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
                    coreLineProcess.innerHTML = `p${processor.runningProcesses[i].id}(${processor.runningProcesses[i].priority})`
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
    getMessageType(messageText) {
        //TODO получение типа сообщения по его тексту (например: поиск слова "добавление" в строке => сообщение о добавлении процесса)
        return 1;
    }
    //
    //
    addEntryToConsole(messageText) {
        let newEntry = this.createElement('p', 'console-container__entry');
        let type = this.getMessageType(messageText);
        switch (type) {
            case 1: {
                break;
            }
            case 2: {
                break;
            }
            //...
        }
        

        newEntry.textContent = messageText;
        this.consoleContainerEntries.appendChild(newEntry);
    }
    //---------------------------------------------------------
    bindAddProcess(handler) {
        this.addingProcessBtn.addEventListener('click', event => {
          if (event.target.className === 'adding-process-form__add-btn') {
            const processName = this.processNameInput.value;
            const processPriority = Number(this.processPriorityInput.value);
            const processWorkTime = Number(this.processWorkTimeInput.value);
            const processArrivalTime = Number(this.processArrivalTimeInput.value);

            // console.log(`processName='${processName}';
            // processPriority='${processPriority}';
            // processWorkTime='${processWorkTime}';
            // processArrivalTime='${processArrivalTime}';
            // `)
        
            if (processName < 0 ||
                processPriority < 0 ||
                processWorkTime < 0 ||
                processArrivalTime < 0) {
                //TODO сделать валидацию формы
                console.log('Данные не введены');
            }
            else {
                handler(processName, processPriority, processWorkTime, processArrivalTime);
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
              this.timerTickTextBlock.classList.toggle('started');
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
    constructor(name, priority, workTime, arrivalTime, remainingWorkTime = workTime, isSentToQueue=false, isCompleted=false, id=AUTO_ID_NUM) {
        if (id == AUTO_ID_NUM) {
            this.id = Process.processCounter++
        }
        else {
            this.id = id;
        }
       
        this.name = name;
        this.priority = priority;
        this.workTime = workTime;
        this.remainingWorkTime = remainingWorkTime;
        this.arrivalTime = arrivalTime;
        this.isSentToQueue = isSentToQueue;
        this.isCompleted = isCompleted;
    }
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
    }
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
    addProcess(name, priority, workTime, arrivalTime=this.timerTick) {
        const newProcess = new Process(name, priority, workTime, arrivalTime);
        this.processList.push(newProcess);
        this.addProcessesInQueue();
        this.onProcessListChanged(this.processList);
        this.onNewOutputAdded(`Добавлен новый процесс (Id=${newProcess.id}).`);
    };
    //подсчитывает свободные (незанятые) ядра
    countFreeCores() {
        let freeCores = 0;
        this.processor.runningProcesses.forEach(process => {
            if (process == null) {
                freeCores++;
            }
        });
        return freeCores;
    }
    //получить самый большой приоритет процесса, находящегося в очереди
    getHighestPriorityOfQueueProcesses() {
        for(let i=MAX_PRIORITY-1; i>0; i--) {
            if (this.processQueuesByPriority[i].length > 0) {
                return {index: i, priority: i};
            }
        }
        return null;
    }
    //получить самый маленький приоритет процесса, находящегося в рантайме
    getLeastPriorityOfRunningProcecess() {
        let process = {index:0, priority: MAX_PRIORITY};
        for (let i=0; i<this.processor.coreNum; i++)
        {
            if (this.processor.runningProcesses[i] != null && this.processor.runningProcesses[i].id != 0) {
                if (this.processor.runningProcesses[i].priority < process.priority) {
                    process.priority = this.processor.runningProcesses[i].priority;
                    process.index = i;
                }
            }
            else {
                return null;
            }
        }
        return process;
        
    }
    //
    takeProcessFromRunningToQueue() {
        for(let i=0; i<this.processor.coreNum; i++) {
            let runningProcessWithLeastPriority = this.getLeastPriorityOfRunningProcecess();
            let queueProcessWithHighestPriority = this.getHighestPriorityOfQueueProcesses();
            //-------------------------------------
            // console.log(`min приоритет в рантайме {ядро:${
            //     runningProcessWithLeastPriority != null ? 
            //     runningProcessWithLeastPriority.index : null}; 
            //     приоритет процесса:${runningProcessWithLeastPriority != null ? 
            //         runningProcessWithLeastPriority.priority : null};}}`)
            // console.log(`max приоритет в очереди {i:${
            //     queueProcessWithHighestPriority != null ? queueProcessWithHighestPriority.index :null}; 
            //     приоритет процесса:${
            //         queueProcessWithHighestPriority != null ? queueProcessWithHighestPriority.priority :null}}`)
            //-------------------------------------
            if (runningProcessWithLeastPriority == null || queueProcessWithHighestPriority == null) {
                return;
            }
            if (runningProcessWithLeastPriority.priority < queueProcessWithHighestPriority.priority) {
                //записали индекс и приоритет процесса (с самым маленьким приоритетом) из рантайма 
                let runProcIndex = runningProcessWithLeastPriority.index;
                let runProcPriority = runningProcessWithLeastPriority.priority;
                let processFromProcessor = this.processor.runningProcesses.splice(runProcIndex, 1)[0];
                // console.log('процесс из рантайма')
                // console.log(JSON.stringify(processFromProcessor))

                //записали индекс и приоритет процесса (с самым большим приоритетом) из очереди
                //let queueProcIndex = queueProcessWithHighestPriority.index;
                let queueProcPriority = queueProcessWithHighestPriority.priority;
                let processFromQueue = this.processQueuesByPriority[queueProcPriority].shift();
                // console.log('процесс из очереди')
                // console.log(JSON.stringify(processFromQueue))
                
                //положили в ядро процессора процесс из очереди
                // console.log('рантайм до того, как туда закинули проц из очереди')
                // console.log(JSON.stringify(this.processor.runningProcesses))
                this.processor.runningProcesses.splice(runProcIndex, 0, processFromQueue);

                // console.log('рантайм после того, как туда закинули проц из очереди')
                // console.log(JSON.stringify(this.processor.runningProcesses))
                //создаем 'псевдо процесс' для того, чтобы этот незавершенный процесс отображался на диаграмме
      
                let subProcess = new Process(
                    processFromProcessor.name, 
                    processFromProcessor.priority, 
                    processFromProcessor.workTime, 
                    processFromProcessor.arrivalTime, 
                    processFromProcessor.remainingWorkTime,
                    processFromProcessor.isSentToQueue, 
                    processFromProcessor.isCompleted, 
                    processFromProcessor.id);

                // console.log('subProcess до')
                // console.log(JSON.stringify(subProcess))
                subProcess.workTime -= subProcess.remainingWorkTime;
                subProcess.remainingWorkTime = 0;
                subProcess.isCompleted = true;
                // console.log('subProcess (его кладем в завершенные)')
                // console.log(JSON.stringify(subProcess))
                //добавление 'псевдо процесса' в массив заверешенных (но он завершен не полностью)
                this.processor.completedProcesses[runProcIndex].push(subProcess);
                // console.log('completedProcesses')
                // console.log(JSON.stringify(this.processor.completedProcesses))
                //подсчет нового приоритета для процесса
                let workTime = processFromProcessor.workTime;
                let completedTime = processFromProcessor.workTime - processFromProcessor.remainingWorkTime;
                let curPriority = processFromProcessor.priority;
                processFromProcessor.priority = Math.round((completedTime/workTime)*curPriority) + curPriority;
                //положили в очередь процесс, который достали из процессора
                processFromProcessor.workTime = processFromProcessor.remainingWorkTime;//уменьшили время работы процесса
                this.processQueuesByPriority[runProcPriority].push(processFromProcessor);

                //
                this.onProcessorPropsChanged(this.processor, this.timerTick);
                this.onProcessQueuesChanged(this.processQueuesByPriority);
                // this.onNewOutputAdded(`Процесс (${process.id}) положили в очередь.`);

            }
        }

    }
    //
    addProcessesToRun() {
        // определение количества свободных (готовых принять новый процесс на выполнение) ядер
        let necessaryProcessesNum = 0;
        for(let j=0; j<this.processor.coreNum; j++) {
            if (this.processor.runningProcesses[j] == null) {
                necessaryProcessesNum++;
            }
        }

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
                }
            }
        }
        if (necessaryProcesses.length == necessaryProcessesNum) {
            this.sendProcessesToProcessor(necessaryProcesses);
            return;
        }
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
        for(let i=0; i<this.processor.coreNum; i++) {
            if (this.processor.runningProcesses[i] == null) {
                let process = processes.shift();
                this.processor.runningProcesses[i] = process;
                this.onNewOutputAdded(`Процесс (${process.id == 0 ? 'пустой процесс' : process.id}) положили в ядро №${i+1}.`);
            }
        }
    };
    //
    startTimer() {
        if (this.timerIsStarted) {
            clearInterval(this.timer);
            this.timerIsStarted = false;
            this.onNewOutputAdded(`Таймер остановлен. Тик: ${this.timerTick}.`);
        }
        else {
            this.onNewOutputAdded(`Таймер запущен. Тик: ${this.timerTick}.`);
            this.timer = setInterval(() => {
                console.log(`\ntimer ${this.timerTick}`)
                // console.log(this.processor);
                this.onNewOutputAdded(`Таймер. Тик: ${this.timerTick}.`);
                //добавление процессов из списка процессов в очередь процессов
                this.addProcessesInQueue();
                //добавление процессов в ядра процессора на выполнение (если очередь пуста - пустыми процессами-заглушками)
                this.addProcessesToRun();
                this.takeProcessFromRunningToQueue();
                //
                this.runProcessForTick();
                
                //событие вызывает перерисовку диаграммы (линии с процессами ядер + линейка)
                this.onProcessorPropsChanged(this.processor, this.timerTick);
                this.timerTick++;
                //событие вызывает перерисовку показателя таймера
                this.onTimerTickChanged(this.timerTick);
                // console.log(this.processor);
                
            }, 1000 * TICK_TIME_IN_SECONDS);
            this.timerIsStarted = true;
        };
    };
    //
    runProcessForTick() {
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
        this.onNewOutputAdded(`Процесс (${process.id}) положили в очередь.`);
    };
    //
    addProcessesInQueue() {
        this.processList.forEach(process => {
            if (!process.isSentToQueue && process.arrivalTime == this.timerTick) {
                process.isSentToQueue = true;
                this.addProcessInQueue(process);
            }
        });
    };
    //-----------------------------------------------------------------------------------
    // бинд - добавлена новая запись
    bindNewOutputAdded(callback) {
        this.onNewOutputAdded = callback;
    }
    // бинд - изменились данные очереди процессов
    bindProcessQueuesChanged(callback) {
        this.onProcessQueuesChanged = callback;
    }
    // бинд - изменились данные списка процессов
    bindProcessListChanged(callback) {
        this.onProcessListChanged = callback;
    };
    // бинд - изменился счётчик таймера
    bindTimerTickChanged(callback) {
        this.onTimerTickChanged = callback;
    };
    // бинд - изменились свойства (данные) процессора
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
      //
      this.model.bindProcessorPropsChanged(this.onProcessorPropsChanged);
      //
      this.model.bindNewOutputAdded(this.onNewOutputAdded);
      //
      
    };
    //
    onNewOutputAdded = messageText => {
        this.view.addEntryToConsole(messageText);
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
    handleAddProcess = (name, workTime, priority, arrivalTime) => {
        this.model.addProcess(name, workTime, priority, arrivalTime);
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

//TMP
app.model.addProcess('proc1', 4, 4, 0);
app.model.addProcess('proc2', 4, 4, 0);
app.model.addProcess('proc3', 4, 4, 0);
app.model.addProcess('proc4', 4, 4, 0);
app.model.addProcess('proc5', 5, 4, 2);
app.model.addProcess('proc6', 5, 4, 2);
app.model.addProcess('proc7', 5, 4, 2);
app.model.addProcess('proc8', 5, 4, 2);
app.model.addProcess('proc9', 6, 4, 4);
app.model.addProcess('proc10', 6, 4, 4);
app.model.addProcess('proc11', 6, 4, 4);
app.model.addProcess('proc12', 6, 4, 4);
app.model.addProcess('proc13', 7, 4, 6);
app.model.addProcess('proc14', 7, 4, 6);
app.model.addProcess('proc15', 7, 4, 6);
app.model.addProcess('proc16', 7, 4, 6);
