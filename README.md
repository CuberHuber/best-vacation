# The Best vacation
[CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

A tool that underpins the best days to take holiday days to find the most profitable and longest permanently holiday sequence.

------

## Whitepaper

### Зачем?
При планировании своего отпуска хочется учесть много факторов (календарные выходные, праздники), личные праздники, предпочтения и число дней, которые мы можем взять как отпускные на будние дни.

### Что?
Инструмент будет предлагать наиболее предпочтительных дней официального отпуска для получения финального самого продолжительного непрерывного отпуска.

### Как?

Обозначим функцию `F(D, W, v, P) -> d's`, где D - непрерывная серия дней (календарь); W - прерывная серия дней государственных выходных дней, отпусков и праздников; v - количество отпускных дней, которые мы можем использовать; P - предпочтения пользователя (личные, семейные праздники, важные дни и тп), `d's` - кортеж дней, на которые нужно взять отпуск.


## Road map

- [ ] Разработать алгоритм
- [ ] Представить удобный UI
- [ ] Интеграция с календарем пользователя
- [ ] Минималистичный и удобный GUI



---------

## Quick start

1. clone repo.
```
git clone https://github.com/CuberHuber/best-vacation.git
```
2. setup python 3.11.* interpreter.
3. install dependencies (via make):
```
make setup
```
or (via classic way):
```
pip install -r requirements.txt
```
4. for testing (via make)
```
make test
```
or (via classic way):
```
pytest -v
```
5. Welcome and let's use the tool
 



