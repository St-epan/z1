import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

abstract class Животные {
    String тип;

    public Животные(String тип) {
        this.тип = тип;
    }

    abstract String получитьИнформацию();
}


class Pets extends Животные {
    String имя;
    String вид;
    Date датаРождения;
    ArrayList<String> команды;

    public Pets(String имя, String вид, Date датаРождения) {
        super("Pets");
        this.имя = имя;
        this.вид = вид;
        this.датаРождения = датаРождения;
        this.команды = new ArrayList<>();
    }

    @Override
    String получитьИнформацию() {
        return "Имя: " + имя + ", Вид: " + вид + ", Дата рождения: " + датаРождения +", Команды: " + команды;
    }


    public void добавитьКоманду(String команда) {
        this.команды.add(команда);
    }
}


class Pack_animals extends Животные {
    String имя;
    String вид;
    Date датаРождения;
    ArrayList<String> команды;

    public Pack_animals(String имя, String вид, Date датаРождения) {
        super("Pack_animals");
        this.имя = имя;
        this.вид = вид;
        this.датаРождения = датаРождения;
        this.команды = new ArrayList<>();
    }
    @Override
    String получитьИнформацию() {
        return  "Имя: " + имя + ", Вид: " + вид + ", Дата рождения: " + датаРождения + ", Команды: " + команды;
    }

    public void добавитьКоманду(String команда) {
        this.команды.add(команда);
    }
}


class Собаки extends Pets {
    String порода;
    String цвет;

    public Собаки(String имя,  Date датаРождения,String порода, String цвет) {
       super(имя, "Собака", датаРождения);
        this.порода = порода;
        this.цвет = цвет;
    }

    @Override
    String получитьИнформацию() {
        return super.получитьИнформацию() + ", Порода: " + порода + ", Цвет: " + цвет;
    }
}

class Кошки extends Pets {
    String порода;
    String цвет;

    public Кошки(String имя, Date датаРождения, String порода, String цвет) {
        super(имя, "Кошка", датаРождения);
        this.порода = порода;
        this.цвет = цвет;
    }
    @Override
    String получитьИнформацию() {
        return super.получитьИнформацию() +", Порода: " + порода + ", Цвет: " + цвет;
    }
}

class Хомяки extends Pets {
    String порода;
    String цвет;

    public Хомяки(String имя, Date датаРождения,String порода, String цвет) {
        super(имя,"Хомяк", датаРождения);
        this.порода = порода;
        this.цвет = цвет;
    }
    @Override
    String получитьИнформацию() {
        return super.получитьИнформацию() + ", Порода: " + порода + ", Цвет: " + цвет;
    }
}



class Лошади extends Pack_animals {
    Double скорость;
    String выносливость;
    public Лошади(String имя, Date датаРождения, Double скорость, String выносливость) {
        super(имя,"Лошадь", датаРождения);
        this.скорость = скорость;
        this.выносливость = выносливость;
    }

    @Override
    String получитьИнформацию() {
        return  super.получитьИнформацию() + ", Скорость: " + скорость + ", Выносливость: " + выносливость;
    }
}

class Верблюды extends Pack_animals {
    Double скорость;
    String выносливость;
    public Верблюды(String имя, Date датаРождения, Double скорость, String выносливость) {
        super(имя, "Верблюд", датаРождения);
        this.скорость = скорость;
        this.выносливость = выносливость;
    }

    @Override
    String получитьИнформацию() {
        return super.получитьИнформацию() + ", Скорость: " + скорость + ", Выносливость: " + выносливость;
    }
}

class Ослы extends Pack_animals {
    Double скорость;
    String выносливость;

    public Ослы(String имя, Date датаРождения,Double скорость, String выносливость) {
        super(имя,"Осел", датаРождения);
        this.скорость = скорость;
        this.выносливость = выносливость;
    }

    @Override
    String получитьИнформацию() {
        return super.получитьИнформацию() + ", Скорость: " + скорость + ", Выносливость: " + выносливость;
    }
}