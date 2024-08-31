#include <iostream>
#include <string>
class Person {
private:
std::string name;

std::string country;

int birthDay;

int birthMonth;

int birthYear;

double height;

double weight;

public:

Person(const std::string& name, const std::string& country, int birthDay, int birthMonth, int birthYear,

double height, double weight)

: name(name), country(country), birthDay(birthDay),birthMonth(birthMonth), birthYear(birthYear),

height(height), weight(weight){}

void display() {

std::cout << "Person Frame:\n";

std::cout << "Name: " << name << std::endl;

std::cout << "Country: " << country << std::endl;

std::cout << "Birthdate: " << birthDay << "th " <<getMonthName(birthMonth) << ", " << birthYear << std::endl;

std::cout << "Height: " << height << " inches" << std::endl;

std::cout << "Weight: " << weight << " kg" << std::endl;

}

std::string getMonthName(int month) {

static const std::string monthNames[] = {

"January", "February", "March", "April", "May", "June","July",

"August", "September", "October", "November", "December"

};

return monthNames[month - 1];

}

};

class Job {

private:

std::string companyName;

std::string position;

double salary;

public:

Job(const std::string& companyName, const std::string& position,double salary)

: companyName(companyName), position(position), salary(salary){}

void display() {

std::cout << "Job Frame:\n";

std::cout << "Company: " << companyName << std::endl;

std::cout << "Position: " << position << std::endl;

std::cout << "Salary: " << salary << " lakhs per month" <<std::endl;

}

};

int main() {

Person* ram = new Person("Ram", "Nepal", 15, 12, 1990, 6, 75);

Job* ramJob = new Job("ABC company", "AI Researcher", 1.5);

ram->display();

std::cout << std::endl;

ramJob->display();

delete ram;
delete ramJob;
return 0;

}

