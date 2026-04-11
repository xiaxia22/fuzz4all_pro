# Class ParserDelegator

**Source:** `java.desktop\javax\swing\text\html\parser\ParserDelegator.html`

### Class Description

```java
public class
ParserDelegator

extends
HTMLEditorKit.Parser

implements
Serializable
```

Responsible for starting up a new DocumentParser
each time its parse method is invoked. Stores a
reference to the dtd.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ParserDelegator()

Creates

ParserDelegator

with default DTD.

---

### Method Details

#### protected static void setDefaultDTD()

Sets the default DTD.

---

#### protected static
DTD
createDTD​(
DTD
dtd,

String
name)

Recreates a DTD from an archived format with the specified

name

.

**Parameters:**
- dtd

- a DTD
- name

- the name of the resource, relative to the ParserDelegator class.

**Returns:**
- the DTD with the specified

name

.

---

### Additional Sections

#### Class ParserDelegator

java.lang.Object

- javax.swing.text.html.HTMLEditorKit.Parser
- - javax.swing.text.html.parser.ParserDelegator

javax.swing.text.html.HTMLEditorKit.Parser

- javax.swing.text.html.parser.ParserDelegator

javax.swing.text.html.parser.ParserDelegator

**All Implemented Interfaces:** Serializable

```java
public class
ParserDelegator

extends
HTMLEditorKit.Parser

implements
Serializable
```

Responsible for starting up a new DocumentParser
each time its parse method is invoked. Stores a
reference to the dtd.

**See Also:** Serialized Form

public class

ParserDelegator

extends

HTMLEditorKit.Parser

implements

Serializable

Responsible for starting up a new DocumentParser
each time its parse method is invoked. Stores a
reference to the dtd.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ParserDelegator

()

Creates

ParserDelegator

with default DTD.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

protected static

DTD

createDTD

​(

DTD

dtd,

String

name)

Recreates a DTD from an archived format with the specified

name

.

protected static void

setDefaultDTD

()

Sets the default DTD.

- Methods declared in class javax.swing.text.html.

HTMLEditorKit.Parser

parse

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

ParserDelegator

()

Creates

ParserDelegator

with default DTD.

---

#### Constructor Summary

Creates

ParserDelegator

with default DTD.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

protected static

DTD

createDTD

​(

DTD

dtd,

String

name)

Recreates a DTD from an archived format with the specified

name

.

protected static void

setDefaultDTD

()

Sets the default DTD.

- Methods declared in class javax.swing.text.html.

HTMLEditorKit.Parser

parse

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

Recreates a DTD from an archived format with the specified

name

.

Sets the default DTD.

Methods declared in class javax.swing.text.html.

HTMLEditorKit.Parser

parse

---

#### Methods declared in class javax.swing.text.html. HTMLEditorKit.Parser

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

- ParserDelegator

```java
public ParserDelegator()
```

Creates

ParserDelegator

with default DTD.

============ METHOD DETAIL ==========

- Method Detail

- setDefaultDTD

```java
protected static void setDefaultDTD()
```

Sets the default DTD.

- createDTD

```java
protected static
DTD
createDTD​(
DTD
dtd,

String
name)
```

Recreates a DTD from an archived format with the specified

name

.

**Parameters:** dtd

- a DTD
**Parameters:** name

- the name of the resource, relative to the ParserDelegator class.
**Returns:** the DTD with the specified

name

.

Constructor Detail

- ParserDelegator

```java
public ParserDelegator()
```

Creates

ParserDelegator

with default DTD.

---

#### Constructor Detail

ParserDelegator

```java
public ParserDelegator()
```

Creates

ParserDelegator

with default DTD.

---

#### ParserDelegator

public ParserDelegator()

Creates

ParserDelegator

with default DTD.

Method Detail

- setDefaultDTD

```java
protected static void setDefaultDTD()
```

Sets the default DTD.

- createDTD

```java
protected static
DTD
createDTD​(
DTD
dtd,

String
name)
```

Recreates a DTD from an archived format with the specified

name

.

**Parameters:** dtd

- a DTD
**Parameters:** name

- the name of the resource, relative to the ParserDelegator class.
**Returns:** the DTD with the specified

name

.

---

#### Method Detail

setDefaultDTD

```java
protected static void setDefaultDTD()
```

Sets the default DTD.

---

#### setDefaultDTD

protected static void setDefaultDTD()

Sets the default DTD.

createDTD

```java
protected static
DTD
createDTD​(
DTD
dtd,

String
name)
```

Recreates a DTD from an archived format with the specified

name

.

**Parameters:** dtd

- a DTD
**Parameters:** name

- the name of the resource, relative to the ParserDelegator class.
**Returns:** the DTD with the specified

name

.

---

#### createDTD

protected static

DTD

createDTD​(

DTD

dtd,

String

name)

Recreates a DTD from an archived format with the specified

name

.

---

