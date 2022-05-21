#include "binaryTree1.h"

int main(int argc, char* argv[])
{
    srand(time(NULL));
    setlocale(LC_ALL, "Rus");
    string in_filneame = "input.dat";
    string out_filneame = "output.dat";

    int n = 0;// Кол-во узлов для записи из файла
    int key = 0; // Ключ
    int level = 0; // Уровень
    char choice; // Выбор
    struct tnode* root;
    root = NULL;

    do
    {
        cout << "Lab 3. Binary trees." << endl;
        printf("\n\t1 - Read file and fill tree;\n\t2 - Save tree in file;\n\t3 - Add element;\n\t4 - Delete tree;\n\t5 - Print tree;\n\t6 - Find and delete node;\n\t0 - Exit:\nYour choice:\t");
        fflush(stdin);
        choice = _getch();
        printf("\n");

        

        switch (choice)
        {
        case '1':
            n = readArrayN(in_filneame);
            cout << "N = " << n << endl;
            randomAdd_N_Nodes(&root, n);
            _getch();
            break;
        case '2':
            clearFile(out_filneame);
            SaveTreeInFile(root, out_filneame);
            cout << "file is written" << endl;
            _getch();
            break;
        case '3':
            while (!(fflush(stdin)) && !(printf("Enter key ") && scanf_s("%d", &key)));//ввод ключа
            root = addNode(root, key);
            _getch();
            break;
        case '4':
            cout << "\nTree will be deleted" << endl;
            deleteSubTree(root);
            root = NULL;
            _getch();
            break;
        case '5':
            if (root) {
                cout << "\nTree:\n";//вывод в прямом порядке
                printTree(root);
                cout << "\nGraphics:\n\n";//вывод в прямом порядке
                printTreeGraphics(root,1);
            }
            else cout << "\nTree is empty:\n";
            _getch();
            break;
        case '6':
            while (!(fflush(stdin)) && !(printf("Enter key to search: ") && scanf_s("%d", &key)));//ввод ключа
            while (!(fflush(stdin)) && !(printf("Enter level to search: ") && scanf_s("%d", &level)));//ввод уровня
            root = deleteNode(root, key, level);
            cout << "removing..." << endl;
            _getch();
            break;
        }

        system("cls");

    } while (choice != '0');



    system("pause");
    return 0;
}