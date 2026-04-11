# Interface FlavorListener

**Source:** `java.datatransfer\java\awt\datatransfer\FlavorListener.html`

### Class Description

```java
public interface
FlavorListener

extends
EventListener
```

Defines an object which listens for

FlavorEvent

s.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void flavorsChanged​(
FlavorEvent
e)

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

Some notifications may be redundant — they are not caused by a
change of the set of DataFlavors available on the clipboard. For example,
if the clipboard subsystem supposes that the system clipboard's contents
has been changed but it can't ascertain whether its DataFlavors have been
changed because of some exceptional condition when accessing the
clipboard, the notification is sent to ensure from omitting a significant
notification. Ordinarily, those redundant notifications should be
occasional.

**Parameters:**
- e

- a

FlavorEvent

object

---

### Additional Sections

#### Interface FlavorListener

**All Superinterfaces:** EventListener

```java
public interface
FlavorListener

extends
EventListener
```

Defines an object which listens for

FlavorEvent

s.

**Since:** 1.5

public interface

FlavorListener

extends

EventListener

Defines an object which listens for

FlavorEvent

s.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

flavorsChanged

​(

FlavorEvent

e)

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

flavorsChanged

​(

FlavorEvent

e)

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

---

#### Method Summary

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

============ METHOD DETAIL ==========

- Method Detail

- flavorsChanged

```java
void flavorsChanged​(
FlavorEvent
e)
```

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

Some notifications may be redundant — they are not caused by a
change of the set of DataFlavors available on the clipboard. For example,
if the clipboard subsystem supposes that the system clipboard's contents
has been changed but it can't ascertain whether its DataFlavors have been
changed because of some exceptional condition when accessing the
clipboard, the notification is sent to ensure from omitting a significant
notification. Ordinarily, those redundant notifications should be
occasional.

**Parameters:** e

- a

FlavorEvent

object

Method Detail

- flavorsChanged

```java
void flavorsChanged​(
FlavorEvent
e)
```

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

Some notifications may be redundant — they are not caused by a
change of the set of DataFlavors available on the clipboard. For example,
if the clipboard subsystem supposes that the system clipboard's contents
has been changed but it can't ascertain whether its DataFlavors have been
changed because of some exceptional condition when accessing the
clipboard, the notification is sent to ensure from omitting a significant
notification. Ordinarily, those redundant notifications should be
occasional.

**Parameters:** e

- a

FlavorEvent

object

---

#### Method Detail

flavorsChanged

```java
void flavorsChanged​(
FlavorEvent
e)
```

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

Some notifications may be redundant — they are not caused by a
change of the set of DataFlavors available on the clipboard. For example,
if the clipboard subsystem supposes that the system clipboard's contents
has been changed but it can't ascertain whether its DataFlavors have been
changed because of some exceptional condition when accessing the
clipboard, the notification is sent to ensure from omitting a significant
notification. Ordinarily, those redundant notifications should be
occasional.

**Parameters:** e

- a

FlavorEvent

object

---

#### flavorsChanged

void flavorsChanged​(

FlavorEvent

e)

Invoked when the target

Clipboard

of the listener has changed its
available

DataFlavor

s.

Some notifications may be redundant — they are not caused by a
change of the set of DataFlavors available on the clipboard. For example,
if the clipboard subsystem supposes that the system clipboard's contents
has been changed but it can't ascertain whether its DataFlavors have been
changed because of some exceptional condition when accessing the
clipboard, the notification is sent to ensure from omitting a significant
notification. Ordinarily, those redundant notifications should be
occasional.

Some notifications may be redundant — they are not caused by a
change of the set of DataFlavors available on the clipboard. For example,
if the clipboard subsystem supposes that the system clipboard's contents
has been changed but it can't ascertain whether its DataFlavors have been
changed because of some exceptional condition when accessing the
clipboard, the notification is sent to ensure from omitting a significant
notification. Ordinarily, those redundant notifications should be
occasional.

---

