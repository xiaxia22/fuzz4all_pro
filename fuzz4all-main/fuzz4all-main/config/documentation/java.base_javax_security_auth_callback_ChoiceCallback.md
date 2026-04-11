# Class ChoiceCallback

**Source:** `java.base\javax\security\auth\callback\ChoiceCallback.html`

### Class Description

```java
public class
ChoiceCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

ChoiceCallback

to the

handle

method of a

CallbackHandler

to display a list of choices
and to retrieve the selected choice(s).

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public ChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

**Parameters:**
- prompt

- the prompt used to describe the list of choices.
- choices

- the list of choices.
- defaultChoice

- the choice to be used as the default choice
when the list of choices are displayed. This value
is represented as an index into the

choices

array.
- multipleSelectionsAllowed

- boolean specifying whether or
not multiple selections can be made from the
list of choices.

**Throws:**
- IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

choices

is null,
if

choices

has a length of 0,
if any element from

choices

is null,
if any element from

choices

has a length of 0 or if

defaultChoice

does not fall within the array boundaries of

choices

.

---

### Method Details

#### public
String
getPrompt()

Get the prompt.

**Returns:**
- the prompt.

---

#### public
String
[] getChoices()

Get the list of choices.

**Returns:**
- the list of choices.

---

#### public int getDefaultChoice()

Get the defaultChoice.

**Returns:**
- the defaultChoice, represented as an index into
the

choices

list.

---

#### public boolean allowMultipleSelections()

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

**Returns:**
- whether multiple selections are allowed.

---

#### public void setSelectedIndex​(int selection)

Set the selected choice.

**Parameters:**
- selection

- the selection represented as an index into the

choices

list.

**See Also:**
- getSelectedIndexes()

---

#### public void setSelectedIndexes​(int[] selections)

Set the selected choices.

**Parameters:**
- selections

- the selections represented as indexes into the

choices

list.

**Throws:**
- UnsupportedOperationException

- if multiple selections are
not allowed, as determined by

allowMultipleSelections

.

**See Also:**
- getSelectedIndexes()

---

#### public int[] getSelectedIndexes()

Get the selected choices.

**Returns:**
- the selected choices, represented as indexes into the

choices

list.

**See Also:**
- setSelectedIndexes(int[])

---

### Additional Sections

#### Class ChoiceCallback

java.lang.Object

- javax.security.auth.callback.ChoiceCallback

javax.security.auth.callback.ChoiceCallback

**All Implemented Interfaces:** Serializable

,

Callback

**Direct Known Subclasses:** RealmChoiceCallback

```java
public class
ChoiceCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

ChoiceCallback

to the

handle

method of a

CallbackHandler

to display a list of choices
and to retrieve the selected choice(s).

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

ChoiceCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

ChoiceCallback

to the

handle

method of a

CallbackHandler

to display a list of choices
and to retrieve the selected choice(s).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ChoiceCallback

​(

String

prompt,

String

[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

allowMultipleSelections

()

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

String

[]

getChoices

()

Get the list of choices.

int

getDefaultChoice

()

Get the defaultChoice.

String

getPrompt

()

Get the prompt.

int[]

getSelectedIndexes

()

Get the selected choices.

void

setSelectedIndex

​(int selection)

Set the selected choice.

void

setSelectedIndexes

​(int[] selections)

Set the selected choices.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ChoiceCallback

​(

String

prompt,

String

[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

---

#### Constructor Summary

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

allowMultipleSelections

()

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

String

[]

getChoices

()

Get the list of choices.

int

getDefaultChoice

()

Get the defaultChoice.

String

getPrompt

()

Get the prompt.

int[]

getSelectedIndexes

()

Get the selected choices.

void

setSelectedIndex

​(int selection)

Set the selected choice.

void

setSelectedIndexes

​(int[] selections)

Set the selected choices.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

Get the list of choices.

Get the defaultChoice.

Get the prompt.

Get the selected choices.

Set the selected choice.

Set the selected choices.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ChoiceCallback

```java
public ChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)
```

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

**Parameters:** prompt

- the prompt used to describe the list of choices.
**Parameters:** choices

- the list of choices.
**Parameters:** defaultChoice

- the choice to be used as the default choice
when the list of choices are displayed. This value
is represented as an index into the

choices

array.
**Parameters:** multipleSelectionsAllowed

- boolean specifying whether or
not multiple selections can be made from the
list of choices.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

choices

is null,
if

choices

has a length of 0,
if any element from

choices

is null,
if any element from

choices

has a length of 0 or if

defaultChoice

does not fall within the array boundaries of

choices

.

============ METHOD DETAIL ==========

- Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

- getChoices

```java
public
String
[] getChoices()
```

Get the list of choices.

**Returns:** the list of choices.

- getDefaultChoice

```java
public int getDefaultChoice()
```

Get the defaultChoice.

**Returns:** the defaultChoice, represented as an index into
the

choices

list.

- allowMultipleSelections

```java
public boolean allowMultipleSelections()
```

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

**Returns:** whether multiple selections are allowed.

- setSelectedIndex

```java
public void setSelectedIndex​(int selection)
```

Set the selected choice.

**Parameters:** selection

- the selection represented as an index into the

choices

list.
**See Also:** getSelectedIndexes()

- setSelectedIndexes

```java
public void setSelectedIndexes​(int[] selections)
```

Set the selected choices.

**Parameters:** selections

- the selections represented as indexes into the

choices

list.
**Throws:** UnsupportedOperationException

- if multiple selections are
not allowed, as determined by

allowMultipleSelections

.
**See Also:** getSelectedIndexes()

- getSelectedIndexes

```java
public int[] getSelectedIndexes()
```

Get the selected choices.

**Returns:** the selected choices, represented as indexes into the

choices

list.
**See Also:** setSelectedIndexes(int[])

Constructor Detail

- ChoiceCallback

```java
public ChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)
```

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

**Parameters:** prompt

- the prompt used to describe the list of choices.
**Parameters:** choices

- the list of choices.
**Parameters:** defaultChoice

- the choice to be used as the default choice
when the list of choices are displayed. This value
is represented as an index into the

choices

array.
**Parameters:** multipleSelectionsAllowed

- boolean specifying whether or
not multiple selections can be made from the
list of choices.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

choices

is null,
if

choices

has a length of 0,
if any element from

choices

is null,
if any element from

choices

has a length of 0 or if

defaultChoice

does not fall within the array boundaries of

choices

.

---

#### Constructor Detail

ChoiceCallback

```java
public ChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)
```

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

**Parameters:** prompt

- the prompt used to describe the list of choices.
**Parameters:** choices

- the list of choices.
**Parameters:** defaultChoice

- the choice to be used as the default choice
when the list of choices are displayed. This value
is represented as an index into the

choices

array.
**Parameters:** multipleSelectionsAllowed

- boolean specifying whether or
not multiple selections can be made from the
list of choices.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if

choices

is null,
if

choices

has a length of 0,
if any element from

choices

is null,
if any element from

choices

has a length of 0 or if

defaultChoice

does not fall within the array boundaries of

choices

.

---

#### ChoiceCallback

public ChoiceCallback​(

String

prompt,

String

[] choices,
int defaultChoice,
boolean multipleSelectionsAllowed)

Construct a

ChoiceCallback

with a prompt,
a list of choices, a default choice, and a boolean specifying
whether or not multiple selections from the list of choices are allowed.

Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

- getChoices

```java
public
String
[] getChoices()
```

Get the list of choices.

**Returns:** the list of choices.

- getDefaultChoice

```java
public int getDefaultChoice()
```

Get the defaultChoice.

**Returns:** the defaultChoice, represented as an index into
the

choices

list.

- allowMultipleSelections

```java
public boolean allowMultipleSelections()
```

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

**Returns:** whether multiple selections are allowed.

- setSelectedIndex

```java
public void setSelectedIndex​(int selection)
```

Set the selected choice.

**Parameters:** selection

- the selection represented as an index into the

choices

list.
**See Also:** getSelectedIndexes()

- setSelectedIndexes

```java
public void setSelectedIndexes​(int[] selections)
```

Set the selected choices.

**Parameters:** selections

- the selections represented as indexes into the

choices

list.
**Throws:** UnsupportedOperationException

- if multiple selections are
not allowed, as determined by

allowMultipleSelections

.
**See Also:** getSelectedIndexes()

- getSelectedIndexes

```java
public int[] getSelectedIndexes()
```

Get the selected choices.

**Returns:** the selected choices, represented as indexes into the

choices

list.
**See Also:** setSelectedIndexes(int[])

---

#### Method Detail

getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt.

---

#### getPrompt

public

String

getPrompt()

Get the prompt.

getChoices

```java
public
String
[] getChoices()
```

Get the list of choices.

**Returns:** the list of choices.

---

#### getChoices

public

String

[] getChoices()

Get the list of choices.

getDefaultChoice

```java
public int getDefaultChoice()
```

Get the defaultChoice.

**Returns:** the defaultChoice, represented as an index into
the

choices

list.

---

#### getDefaultChoice

public int getDefaultChoice()

Get the defaultChoice.

allowMultipleSelections

```java
public boolean allowMultipleSelections()
```

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

**Returns:** whether multiple selections are allowed.

---

#### allowMultipleSelections

public boolean allowMultipleSelections()

Get the boolean determining whether multiple selections from
the

choices

list are allowed.

setSelectedIndex

```java
public void setSelectedIndex​(int selection)
```

Set the selected choice.

**Parameters:** selection

- the selection represented as an index into the

choices

list.
**See Also:** getSelectedIndexes()

---

#### setSelectedIndex

public void setSelectedIndex​(int selection)

Set the selected choice.

setSelectedIndexes

```java
public void setSelectedIndexes​(int[] selections)
```

Set the selected choices.

**Parameters:** selections

- the selections represented as indexes into the

choices

list.
**Throws:** UnsupportedOperationException

- if multiple selections are
not allowed, as determined by

allowMultipleSelections

.
**See Also:** getSelectedIndexes()

---

#### setSelectedIndexes

public void setSelectedIndexes​(int[] selections)

Set the selected choices.

getSelectedIndexes

```java
public int[] getSelectedIndexes()
```

Get the selected choices.

**Returns:** the selected choices, represented as indexes into the

choices

list.
**See Also:** setSelectedIndexes(int[])

---

#### getSelectedIndexes

public int[] getSelectedIndexes()

Get the selected choices.

---

