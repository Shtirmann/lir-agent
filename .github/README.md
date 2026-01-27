# lir-agent

---

![License](https://img.shields.io/github/license/Mawwlle/lir-agent?style=flat&logo=opensourceinitiative&logoColor=white&color=blue)
[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

---

## Overview

lir-agent — это интеллектуальный помощник, который улучшает свои возможности решения задач, динамически создавая и используя новые инструменты. Он адаптируется в реальном времени к потребностям пользователя, предлагая гибкое и самоулучшающееся решение для сложных задач через рассуждение и действие.

---

## Table of Contents

- [Overview](#overview)
- [Core Features](#core-features)
- [Installation](#installation)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)

---

## Core Features

1. **Создание инструментов во время выполнения**: Агент может динамически создавать новые инструменты на Python во время выполнения, генерируя код на Python, сохраняя его в файл, импортируя как модуль и регистрируя его точку входа для последующего использования. Это позволяет агенту адаптироваться и расширять свои возможности на лету.
2. **Динамическое выполнение инструментов**: Агент может динамически выполнять любой зарегистрированный инструмент по его имени, передавая аргументы по мере необходимости. Это позволяет агенту беспрепятственно использовать как предопределенные, так и вновь созданные инструменты в своем рабочем процессе.
3. **Управление зависимостями**: Агент включает инструмент для установки пакетов Python в своей виртуальной среде. Это гарантирует, что любые новые инструменты, созданные или используемые агентом, могут иметь свои необходимые зависимости без ручного вмешательства.
4. **Цикл агента ReAct**: Агент работает на основе цикла ReAct (Reasoning and Acting), где он следует последовательности Мысль → Действие → Наблюдение. Этот структурированный подход направляет агента в решении задач, создании инструментов и их использовании.
5. **Интеграция LLM (LangChain)**: Агент использует LangChain для интеграции с большими языковыми моделями (LLM), в частности ChatOpenAI. Это позволяет агенту понимать естественные языковые подсказки, рассуждать о задачах и генерировать соответствующие действия, включая создание и использование инструментов.

---

## Installation

**Требования:** требуется Python >=3.12

Установите lir-agent, используя один из следующих методов:

**Сборка из исходного кода:**

1. Клонируйте репозиторий lir-agent:
```sh
git clone https://github.com/Mawwlle/lir-agent
```

2. Перейдите в каталог проекта:
```sh
cd lir-agent
```

3. Установите зависимости проекта:

```sh
pip install -r requirements.txt
```

---

## Documentation

Подробное описание lir-agent доступно [здесь]("").

---

## Contributing

- **[Сообщить о проблемах](https://github.com/Mawwlle/lir-agent/issues)**: Сообщайте об обнаруженных ошибках или оставляйте запросы на добавление функций для проекта.

- **[Отправить запросы на слияние](https://github.com/Shtirmann/lir-agent/tree/master/.github/CONTRIBUTING.md)**: Узнайте больше о том, как внести вклад в lir-agent.

---

## License

Этот проект защищен лицензией MIT. Для получения более подробной информации обратитесь к файлу [LICENSE](https://github.com/Mawwlle/lir-agent/tree/master/LICENSE).

---

## Citation

Если вы используете это программное обеспечение, пожалуйста, цитируйте его следующим образом.

### Формат APA:

    Mawwlle (2026). lir-agent repository [Computer software]. https://github.com/Mawwlle/lir-agent

### Формат BibTeX:

    @misc{lir-agent,
        author = {Mawwlle},
        title = {lir-agent repository},
        year = {2026},
        publisher = {github.com},
        journal = {github.com repository},
        howpublished = {\url{https://github.com/Mawwlle/lir-agent.git}},
        url = {https://github.com/Mawwlle/lir-agent.git}
    }
