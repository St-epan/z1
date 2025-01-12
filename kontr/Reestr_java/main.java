import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

// Базовый класс Animal
abstract class Animal {
    protected String name;
    protected String birthDate;
    protected ArrayList<String> commands;

    public Animal(String name, String birthDate) {
        this.name = name;
        this.birthDate = birthDate;
        this.commands = new ArrayList<>();
    }

    public abstract String getAnimalType();

    public void addCommand(String command) {
        commands.add(command);
    }

    public ArrayList<String> getCommands() {
        return commands;
    }

    public String getBirthDate() {
        return birthDate;
    }
}

// Подкласс Dog
class Dog extends Animal {
    public Dog(String name, String birthDate) {
        super(name, birthDate);
    }

    @Override
    public String getAnimalType() {
        return "Собака";
    }
}

// Подкласс Cat
class Cat extends Animal {
    public Cat(String name, String birthDate) {
        super(name, birthDate);
    }

    @Override
    public String getAnimalType() {
        return "Кошка";
    }
}

// Менеджер реестра животных
class AnimalRegistry {
    private ArrayList<Animal> animals;
    private int animalCount;

    public AnimalRegistry() {
        animals = new ArrayList<>();
        animalCount = 0;
    }

    public void addAnimal(Animal animal) {
        animals.add(animal);
        animalCount++;
    }

    public int getAnimalCount() {
        return animalCount;
    }

    public void listAnimalsByBirthDate() {
        Collections.sort(animals, new Comparator<Animal>() {
            public int compare(Animal a1, Animal a2) {
                return a1.getBirthDate().compareTo(a2.getBirthDate());
            }
        });

        for (Animal animal : animals) {
            System.out.println(animal.getAnimalType() + ": " + animal.name + ", Дата рождения: " + animal.getBirthDate());
        }
    }

    public ArrayList<Animal> getAnimals() {
        return animals;
    }
}

// Основной класс программы
public class AnimalRegistryApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AnimalRegistry registry = new AnimalRegistry();
        boolean running = true;

        while (running) {
            System.out.println("Выберите действие:");
            System.out.println("1. Добавить новое животное");
            System.out.println("2. Список команд животного");
            System.out.println("3. Обучить новое животное команде");
            System.out.println("4. Вывести список животных по дате рождения");
            System.out.println("5. Показать общее количество животных");
            System.out.println("6. Выход");
            System.out.print("Ваш выбор: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Удалите символ новой строки

            switch (choice) {
                case 1:
                    System.out.print("Введите тип животного (собака, кошка): ");
                    String type = scanner.nextLine();
                    System.out.print("Введите имя животного: ");
                    String name = scanner.nextLine();
                    System.out.print("Введите дату рождения (YYYY-MM-DD): ");
                    String birthDate = scanner.nextLine();

                    if (type.equalsIgnoreCase("собака")) {
                        registry.addAnimal(new Dog(name, birthDate));
                    } else if (type.equalsIgnoreCase("кошка")) {
                        registry.addAnimal(new Cat(name, birthDate));
                    } else {
                        System.out.println("Неверный тип животного.");
                    }
                    break;

                case 2:
                     
                    System.out.print("Введите имя животного: ");
                    String animalName = scanner.nextLine();
                    Animal foundAnimal = null;
                    for (Animal animal : registry.getAnimals()) {
                        if (animal.name.equals(animalName)) {
                            foundAnimal = animal;
                            break;
                        }
                    }
                    if (foundAnimal != null) {
                        System.out.println("Список команд для " + foundAnimal.name + ": " + foundAnimal.getCommands());
                    } else {
                        System.out.println("Животное не найдено.");
                    }
                    break;

                case 3:
                    System.out.print("Введите имя животного: ");
                    String nameToTrain = scanner.nextLine();
                    System.out.print("Введите новую команду: ");
                    String command = scanner.nextLine();
                    for (Animal animal : registry.getAnimals()) {
                        if (animal.name.equals(nameToTrain)) {
                            animal.addCommand(command);
                            System.out.println("Команда добавлена.");
                            break;
                        }
                    }
                    break;

                case 4:
                    registry.listAnimalsByBirthDate();
                    break;

                case 5:
                    System.out.println("Общее количество животных: " + registry.getAnimalCount());
                    break;

                case 6:
                    running = false;
                    break;

                default:
                    System.out.println("Неверный выбор. Попробуйте снова.");
            }
        }

        scanner.close();
    }
}

