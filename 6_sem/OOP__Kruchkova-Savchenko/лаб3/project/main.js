
const RUS_LANG_QUESTIONS_FILENAME = 'rus_lang_questions.json';
const ENGLISH_WORDS_TRANSLATION_FILENAME = 'english_words.json';
const GAMER_STAT = 'gamer_stat.json';
const MATH_GAME_NAME = "Математика";
const RUS_LANG_GAME_NAME = "Русский язык";
const ENGLISH_WORDS_GAME_NAME = "Английский язык";

const INIT_STAT_ARRAY = {
    gameNumber: 3,
    games: [
        {
            gameName: MATH_GAME_NAME,
            experience: 0,
            answeredExercisesNum: 0,
        },
        {
            gameName: RUS_LANG_GAME_NAME,
            experience: 0,
            answeredExercisesNum: 0,
        },
        {
            gameName: ENGLISH_WORDS_GAME_NAME,
            experience: 0,
            answeredExercisesNum: 0,
        }
    ]
}

const MATH_GAME_CONFIG = {
    experienceForOneExercise: 100,
    minNumber: -10,
    maxNumber: 10,
}

const RUS_LANG_CONFIG = {
    experienceForOneExercise: 100,
}

const ENGLISH_WORDS_GAME_CONFIG = {
    experienceForOneExercise: 50,
}

// получение произвольного случайного числа
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

// класс Конфигурации игры
class GameConfig {

    #gameConfig;

    constructor(_gameConfig) {
        this.#gameConfig = _gameConfig;
    }
    
    changeGameConfig(gameConfig) {
        // TODO изменение конфига
    }

    writeConfigInFile(filename) {
        // TODO запись объекта в json файл
    }

    readConfigFromFile(filename) {
        // TODO чтение объекта json файла в переменную
    }

    // getters и setters
    
    get gameConfig() {
        return this.#gameConfig;
    }

    set gameConfig(value) {
        this.#gameConfig = value;
    }
}

//класс Статистика игрока
class GamesStat {

    #gamesStat;

    constructor(_gamesStat) {
        this.#gamesStat = [];
        for(let i=0 ; i < _gamesStat.gameNumber; i++) {
            this.gamesStat.push(_gamesStat.games[i]);
        }
    }

    changeGameStat(gameName, experience, exercises) {
        gameNum = this.gamesStat.gameNumber;
        for(let i=0; i < gameNum; i++) {
            if (this.gamesStat.games[i].gameName == gameName) {
                this.gamesStat.games[i].experience = experience;
                this.gamesStat.games[i].answeredExercisesNum = exercises;
            }
        }
    }

    writeStatInFile(filename) {
        // TODO запись объекта в json файл
    }

    readStatFromFile(filename) {
        // TODO чтение объекта json файла в переменную
    }

    // getters и setters
    
    get gamesStat() {
        return this.#gamesStat;
    }

    set gamesStat(value) {
        this.#gamesStat = value;
    }
}

// класс Игрок
class Player {

    #nickname;
    #gamesStat;

    constructor(_nickname, _gamesStat) {
        this.#nickname = _nickname;
        this.#gamesStat = new GamesStat(_gamesStat);
    }

    changeNickname(_nickname) {
        this.nickname = _nickname;
    }

    // getters и setters
    
    get nickname() {
        return this.#nickname;
    }

    set nickname(value) {
        this.#nickname = value;
    }

    get gamesStat() {
        return this.#gamesStat;
    }

    set gamesStat(value) {
        this.#gamesStat = value;
    }
}

// класс игра
class Game {

    #playerAnswer; //ответ пользователя
    #correctAnswer; //правильный ответ
    #name;
    #experience;
    #experienceForOneExercise;
    #answeredExercisesNum;
    
    constructor(gameStat, gameConfig) {
        this.#name = gameStat.name;
        this.#experience = gameStat.experience; //инит кол-ва опыта
        this.#experienceForOneExercise = gameConfig.experienceForOneExercise; //инит кол-ва опыта за прохождение 1 упражнения (вопроса)
        this.#answeredExercisesNum = gameStat.addAnsweredExercises; //кол-во отвеченных заданий (вопросов/слов/примеров...)
    }

    displayAnswerResultMessage(isAnswerTrue) {
        if (isAnswerTrue) {
            console.log('Правильный ответ :)');
            // TODO вывод popup в пользовательском интерфейсе
        }
        else {
            console.log('Неправильный ответ :(');
            // TODO вывод popup в пользовательском интерфейсе
        }
    }

    goToNextLevel() {
        console.log('Перешли на следующий уровень!');
        // TODO переход на следующий уровень в интерфейсе
    }

    #addExperience() {
        console.log('Добавили опыта!')
        this.experience += this.experienceForOneExercise;
        // TODO добавление опыта текущему игроку
    }

    #addAnsweredExercises() {
        console.log('Прошли ещё одно задание!')
        this.answeredExercisesNum += 1;
    }

    checkCorrectAnswer() {
        if (this.playerAnswer == this.correctAnswer) {
            this.#addAnsweredExercises();
            this.#addExperience();
            return true;
        }
        else return false;
    }

    // getters и setters
    
    get experience() {
        return this.#experience;
    }

    set experience(value) {
        this.#experience = value;
    }

    get answeredExercisesNum() {
        return this.#answeredExercisesNum;
    }

    set answeredExercisesNum(value) {
        this.#answeredExercisesNum = value;
    }

    get experienceForOneExercise() {
        return this.#experienceForOneExercise;
    }

    set experienceForOneExercise(value) {
        this.#experienceForOneExercise = value;
    }
 
    get correctAnswer() {
        return this.#correctAnswer;
    }

    set correctAnswer(value) {
        this.#correctAnswer = value;
    }

    get playerAnswer() {
        return this.#playerAnswer;
    }

    set playerAnswer(value) {
        this.#playerAnswer = value;
    } 

    // сеттера для имени игры нет
    get name() {
        return this.#name;
    }
}

// класс Математическая игра
class MathGame extends Game {

    #minNumber;
    #maxNumber;
    #curRandNum1;
    #curRandNum2;

    constructor(gameStat, gameConfig) {
        super.constructor(gameStat, gameConfig);
        this.#minNumber = gameConfig.minNumber;
        this.#maxNumber = gameConfig.maxNumber;
        this.#curRandNum1 = 0; //инит случайного числа 1
        this.#curRandNum2 = 0; //инит случайного числа 2
    }

    generateRandomNums() {
        this.curRandNum1 = getRandomArbitrary(this.minNumber, this.maxNumber);
        this.curRandNum2 = getRandomArbitrary(this.minNumber, this.maxNumber);
    }

    countRandNumsSum() {
        this.correctAnswer = this.curRandNum1 + this.curRandNum2
    }

    displayAsk() {
        console.log('Какова сумма чисел (' + str(this.curRandNum1) + ') и (' + str(this.curRandNum2) + ')?');
        // TODO вывод вопроса в интерфейса
    }

    // getters и setters

    get minNumber() {
        return this.#minNumber;
    }

    set minNumber(value) {
        this.#minNumber = value;
    }

    get maxNumber() {
        return this.#maxNumber;
    }

    set maxNumber(value) {
        this.#maxNumber = value;
    }

    get curRandNum1() {
        return this.#curRandNum1;
    }

    set curRandNum1(value) {
        this.#curRandNum1 = value;
    }

    get curRandNum2() {
        return this.#curRandNum2;
    }

    set curRandNum2(value) {
        this.#curRandNum2 = value;
    }
    
}

// класс Игра на знания русского языка
class RusLangGame extends Game {
    #ask;
    #answers;
    constructor(gameStat, gameConfig) {
        super.constructor(gameStat, gameConfig);
        this.#ask = ''; //инит вопроса
        this.#answers = Array(); //инит списка ответов
    }

    getAskFromFile(filename) {
        // TODO получение вопроса из файла
        question = '';
        return question;
    }

    shuffleAnswers() {
        // TODO перемешать ответы
    }

    displayAsk() {
        console.log('Вопрос: ' + str(this.ask) + ' Варианты ответов: ' + str(this.answers));
        // TODO вывод вопроса в интерфейса
    }

    // getters и setters

    get ask() {
        return this.#ask;
    }

    set ask(value) {
        this.#ask= value;
    }

    get answers() {
        return this.#answers;
    }

    set answers(value) {
        this.#answers = value;
    }  
}

// класс Игра на изучение английского языка
class EnglishWordsGame extends Game {
    #word;
    #isFromEnglishToRussian;
    constructor(gameStat, gameConfig) {
        super.constructor(gameStat, gameConfig);
        this.#word = ''; //инит слова
        this.#isFromEnglishToRussian = true; //инит режима: с английского на русский (при false наоборот)
    }

    getWordPairFromFile(filename) {
        // TODO получение слова и его перевода из файла
        this.word = '';
        this.correctAnswer = ''; //правильный ответ (перевод слова)
        question = '';
        return question;
    }

    showCard() {
        console.log('Слово: ' + str(this.word) + '; Перевод на обратной стороне: ' + str(this.wordTranslation));
        // TODO вывод слова в интерфейсе
    }

    rotateCard() {
        // TODO поворот карточки (на обратное стороне перевод)
    }
    
    // getters и setters

    get word() {
        return this.#word;
    }

    set word(value) {
        this.#word = value;
    } 

    get isFromEnglishToRussian() {
        return this.#isFromEnglishToRussian;
    }

    set isFromEnglishToRussian(value) {
        this.#isFromEnglishToRussian = value;
    }
}