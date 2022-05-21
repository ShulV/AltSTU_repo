#include "pch.h"
#include "CppUnitTest.h"
#include "..\lab2_linked_lists\lab2_linked_lists.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace ListMethodsTests
{
	TEST_CLASS(GetSizeTests)
	{
	public:
		
		TEST_METHOD(list_0elem)
		{
			List<int> lst;
			Assert::AreEqual(0, lst.GetSize());
		}
		TEST_METHOD(list_100elem)
		{
			List<int> lst;
			for (int i = 0; i < 100; i++) {
				lst.push_back(rand() % 500 - 250);
			}
			Assert::AreEqual(100, lst.GetSize());
		}
		TEST_METHOD(list_1elem)
		{
			List<int> lst;
			lst.push_back(44);
			Assert::AreEqual(1, lst.GetSize());
		}
	};
	TEST_CLASS(RemoveAtTests)
	{
	public:

		TEST_METHOD(push1_remove1)
		{
			List<int> lst;
			lst.push_back(44);
			lst.removeAt(1);
			Assert::AreEqual(0, lst.GetSize());
		}
		TEST_METHOD(push100_remove100)
		{
			List<int> lst;
			for (int i = 0; i < 100; i++) {
				lst.push_back(rand() % 500 - 250);
			}
			for (int i = 0; i < 100; i++) {
				lst.removeAt(0);
			}
			Assert::AreEqual(0, lst.GetSize());
		}
		TEST_METHOD(remove_from_middle_of_list)
		{
			List<int> lst;
			for (int i = 0; i < 5; i++) {
				lst.push_back(i);
			}
			for (int i = 0; i < 3; i++) {
				lst.removeAt(1);
			}
			Assert::AreEqual(4, lst[1]);
		}
	};
	TEST_CLASS(PushBackTests)
	{
	public:

		TEST_METHOD(push_back_3_times)
		{
			List<int> lst;
			lst.push_back(11);
			lst.push_back(22);
			lst.push_back(33);
			Assert::AreEqual(lst[0], 11);
			Assert::AreEqual(lst[1], 22);
			Assert::AreEqual(lst[2], 33);
		}
		TEST_METHOD(is_null)
		{
			List<int> lst;

			lst.push_back(11);
			lst.removeAt(0);
			
			Assert::AreEqual(0, lst.GetSize());

			lst.push_back(333);
			Assert::AreEqual(1, lst.GetSize());
			
		}
	};
}
