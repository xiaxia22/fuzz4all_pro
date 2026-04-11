# Class RealmChoiceCallback

**Source:** `java.security.sasl\javax\security\sasl\RealmChoiceCallback.html`

### Class Description

```java
public class
RealmChoiceCallback

extends
ChoiceCallback
```

This callback is used by

SaslClient

and

SaslServer

to obtain a realm given a list of realm choices.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public RealmChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multiple)

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

**Parameters:**
- prompt

- the non-null prompt to use to request the realm.
- choices

- the non-null list of realms to choose from.
- defaultChoice

- the choice to be used as the default choice
when the list of choices is displayed. It is an index into
the

choices

array.
- multiple

- true if multiple choices allowed; false otherwise

**Throws:**
- IllegalArgumentException

- If

prompt

is null or the empty string,
if

choices

has a length of 0, if any element from

choices

is null or empty, or if

defaultChoice

does not fall within the array boundary of

choices

---

### Method Details

*No entries found.*

### Additional Sections

#### Class RealmChoiceCallback

java.lang.Object

- javax.security.auth.callback.ChoiceCallback
- - javax.security.sasl.RealmChoiceCallback

javax.security.auth.callback.ChoiceCallback

- javax.security.sasl.RealmChoiceCallback

javax.security.sasl.RealmChoiceCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
RealmChoiceCallback

extends
ChoiceCallback
```

This callback is used by

SaslClient

and

SaslServer

to obtain a realm given a list of realm choices.

**Since:** 1.5
**See Also:** Serialized Form

public class

RealmChoiceCallback

extends

ChoiceCallback

This callback is used by

SaslClient

and

SaslServer

to obtain a realm given a list of realm choices.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RealmChoiceCallback

​(

String

prompt,

String

[] choices,
int defaultChoice,
boolean multiple)

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.security.auth.callback.

ChoiceCallback

allowMultipleSelections

,

getChoices

,

getDefaultChoice

,

getPrompt

,

getSelectedIndexes

,

setSelectedIndex

,

setSelectedIndexes

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

RealmChoiceCallback

​(

String

prompt,

String

[] choices,
int defaultChoice,
boolean multiple)

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

---

#### Constructor Summary

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

Method Summary

- Methods declared in class javax.security.auth.callback.

ChoiceCallback

allowMultipleSelections

,

getChoices

,

getDefaultChoice

,

getPrompt

,

getSelectedIndexes

,

setSelectedIndex

,

setSelectedIndexes

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

Methods declared in class javax.security.auth.callback.

ChoiceCallback

allowMultipleSelections

,

getChoices

,

getDefaultChoice

,

getPrompt

,

getSelectedIndexes

,

setSelectedIndex

,

setSelectedIndexes

---

#### Methods declared in class javax.security.auth.callback. ChoiceCallback

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

- RealmChoiceCallback

```java
public RealmChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multiple)
```

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

**Parameters:** prompt

- the non-null prompt to use to request the realm.
**Parameters:** choices

- the non-null list of realms to choose from.
**Parameters:** defaultChoice

- the choice to be used as the default choice
when the list of choices is displayed. It is an index into
the

choices

array.
**Parameters:** multiple

- true if multiple choices allowed; false otherwise
**Throws:** IllegalArgumentException

- If

prompt

is null or the empty string,
if

choices

has a length of 0, if any element from

choices

is null or empty, or if

defaultChoice

does not fall within the array boundary of

choices

Constructor Detail

- RealmChoiceCallback

```java
public RealmChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multiple)
```

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

**Parameters:** prompt

- the non-null prompt to use to request the realm.
**Parameters:** choices

- the non-null list of realms to choose from.
**Parameters:** defaultChoice

- the choice to be used as the default choice
when the list of choices is displayed. It is an index into
the

choices

array.
**Parameters:** multiple

- true if multiple choices allowed; false otherwise
**Throws:** IllegalArgumentException

- If

prompt

is null or the empty string,
if

choices

has a length of 0, if any element from

choices

is null or empty, or if

defaultChoice

does not fall within the array boundary of

choices

---

#### Constructor Detail

RealmChoiceCallback

```java
public RealmChoiceCallback​(
String
prompt,

String
[] choices,
int defaultChoice,
boolean multiple)
```

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

**Parameters:** prompt

- the non-null prompt to use to request the realm.
**Parameters:** choices

- the non-null list of realms to choose from.
**Parameters:** defaultChoice

- the choice to be used as the default choice
when the list of choices is displayed. It is an index into
the

choices

array.
**Parameters:** multiple

- true if multiple choices allowed; false otherwise
**Throws:** IllegalArgumentException

- If

prompt

is null or the empty string,
if

choices

has a length of 0, if any element from

choices

is null or empty, or if

defaultChoice

does not fall within the array boundary of

choices

---

#### RealmChoiceCallback

public RealmChoiceCallback​(

String

prompt,

String

[] choices,
int defaultChoice,
boolean multiple)

Constructs a

RealmChoiceCallback

with a prompt, a list of
choices and a default choice.

---

