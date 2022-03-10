const MIN_MATH_GAME_NUMBER = -10;
const MAX_MATH_GAME_NUMBER = 10;
const EXPERIENCE_FOR_ONE_EXERCISE_IN_MATH_GAME = 100;
const EXPERIENCE_FOR_ONE_EXERCISE_IN_RUS_LANG_GAME = 100;
const EXPERIENCE_FOR_ONE_EXERCISE_IN_ENGLISH_WORDS_GAME = 50;
const RUS_LANG_QUESTIONS_FILENAME = 'rus_lang_questions.json';
const ENGLISH_WORDS_TRANSLATION_FILENAME = 'english_words.json';

// получение произвольного случайного числа
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

// класс Игрок
class Player {

    constructor(nickname) {
        this.#nickname = nickname;
    }

    get nickname() {
        return this.#nickname;
    }

    set nickname(value) {
        this.#nickname = value;
    }
}

// класс игра
class Game {

    constructor() {
        this.#experience = 0; //инит кол-ва опыта
        this.#experienceForOneExercise = 0; //инит кол-ва опыта за прохождение 1 упражнения (вопроса)
        this.#exercisesAnsweredNum = 0; //кол-во отвеченных заданий (вопросов/слов/примеров...)
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

    addExperience() {
        console.log('Добавили опыта!')
        this.experience += this.experienceForOneExercise;
        // TODO добавление опыта текущему игроку
    }

    
    addAnsweredExercises() {
        console.log('Прошли ещё одно задание!')
        this.exercisesAnsweredNum += 1;
    }

    // getters и setters
    
    get experience() {
        return this.#experience;
    }

    set experience(value) {
        this.#experience = value;
    }

    get exercisesAnsweredNum() {
        return this.#exercisesAnsweredNum;
    }

    set exercisesAnsweredNum() {
        this.#exercisesAnsweredNum = value;
    }
}

// класс Математическая игра
class MathGame extends Game {

    constructor() {
        super.constructor();
        this.#minNumber = MIN_MATH_GAME_NUMBER;
        this.#maxNumber = MAX_MATH_GAME_NUMBER;
        this.#experienceForOneExercise = EXPERIENCE_FOR_ONE_EXERCISE_IN_MATH_GAME;
        this.#curRandNum1 = 0; //инит случайного числа 1
        this.#curRandNum2 = 0; //инит случайного числа 2
        this.#playerAnswer = 0; //инит ответа суммы
    }

    generateRandomNums() {
        this.curRandNum1 = getRandomArbitrary(this.minNumber, this.maxNumber);
        this.curRandNum2 = getRandomArbitrary(this.minNumber, this.maxNumber);
    }

    displayAsk() {
        console.log('Какова сумма чисел (' + str(this.curRandNum1) + ') и (' + str(this.curRandNum2) + ')?');
        // TODO вывод вопроса в интерфейса
    }

    checkCorrectAnswer() {
        sum = this.curRandNum1 + this.curRandNum2;
        if (this.playerAnswer == sum) {
            this.addAnsweredExercises();
            this.addExperience();
            return true;
        }
        else return false;
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

    get experienceForOneExercise() {
        return this.#experienceForOneExercise;
    }

    set experienceForOneExercise(value) {
        this.#experienceForOneExercise = value;
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

    get playerAnswer() {
        return this.#playerAnswer;
    }

    set playerAnswer(value) {
        this.#playerAnswer = value;
    }
    
}

// класс Игра на знания русского языка
class RusLangGame extends Game {

    constructor() {
        super.constructor();
        this.#experienceForOneExercise = EXPERIENCE_FOR_ONE_EXERCISE_IN_RUS_LANG_GAME;
        this.#ask = ''; //инит вопроса
        this.#answers = Array(); //инит списка ответов
        this.#correctAnswer = ''; //инит правильного ответа
        this.#playerAnswer = ''; //инит ответа на вопрос
    }

    getAskFromFile(RUS_LANG_QUESTIONS_FILENAME) {
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

    checkCorrectAnswer() {
        if (this.playerAnswer == this.correctAnswer) {
            this.addAnsweredExercises();
            this.addExperience();
            return true;
        }
        else return false;
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
}

// класс Игра на изучение английского языка
class EnglishWordsGame extends Game {
    constructor() {
        super.constructor();
        this.#experienceForOneExercise = EXPERIENCE_FOR_ONE_EXERCISE_IN_ENGLISH_WORDS_GAME;
        this.#word = ''; //инит слова
        this.#wordTranslation = ''; //инит перевода слова
        this.#playerAnswer = ''; //инит ответа с переводом
        this.#isFromEnglishToRussian = true; //инит режима: с английского на русский (при false наоборот)
    }

    getWordFromFile(ENGLISH_WORDS_TRANSLATION_FILENAME) {
        // TODO получение слова и его перевода из файла
        word = '';
        wordTranslation = '';
        return question;
    }

    displayAsk() {
        console.log('Слово: ' + str(this.word) + '; Перевод на обратной стороне: ' + str(this.wordTranslation));
        // TODO вывод слова в интерфейса
    }

    rotateCard() {
        // TODO поворот карточки (на обратное стороне перевод)
    }

    checkCorrectAnswer() {
        if (this.playerAnswer == this.wordTranslation) {
            this.addAnsweredExercises();
            this.addExperience();
            return true;
        }
        else return false;
    }
    
    // getters и setters

    get word() {
        return this.#word;
    }

    set word(value) {
        this.#word = value;
    } 

    get wordTranslation() {
        return this.#wordTranslation;
    }

    set wordTranslation(value) {
        this.#wordTranslation = value;
    } 

    get playerAnswer() {
        return this.#playerAnswer;
    }

    set playerAnswer(value) {
        this.#playerAnswer = value;
    }

    get isFromEnglishToRussian() {
        return this.#isFromEnglishToRussian;
    }

    set isFromEnglishToRussian(value) {
        this.#isFromEnglishToRussian = value;
    }
}