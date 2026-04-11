# Class HTMLEditorKit.Parser

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.Parser.html`

### Class Description

```java
public abstract static class
HTMLEditorKit.Parser

extends
Object
```

Interface to be supported by the parser. This enables
providing a different parser while reusing some of the
implementation provided by this editor kit.

**Direct Known Subclasses:** ParserDelegator

---

### Field Details

*No entries found.*

### Constructor Details

#### public Parser()

*No description found.*

---

### Method Details

#### public abstract void parse​(
Reader
r,

HTMLEditorKit.ParserCallback
cb,
boolean ignoreCharSet)
throws
IOException

Parse the given stream and drive the given callback
with the results of the parse. This method should
be implemented to be thread-safe.

**Parameters:**
- r

- a reader
- cb

- a parser callback
- ignoreCharSet

- if

true

charset is ignoring

**Throws:**
- IOException

- if an I/O exception occurs

---

### Additional Sections

#### Class HTMLEditorKit.Parser

java.lang.Object

- javax.swing.text.html.HTMLEditorKit.Parser

javax.swing.text.html.HTMLEditorKit.Parser

**Direct Known Subclasses:** ParserDelegator

**Enclosing class:** HTMLEditorKit

```java
public abstract static class
HTMLEditorKit.Parser

extends
Object
```

Interface to be supported by the parser. This enables
providing a different parser while reusing some of the
implementation provided by this editor kit.

public abstract static class

HTMLEditorKit.Parser

extends

Object

Interface to be supported by the parser. This enables
providing a different parser while reusing some of the
implementation provided by this editor kit.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Parser

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

parse

​(

Reader

r,

HTMLEditorKit.ParserCallback

cb,
boolean ignoreCharSet)

Parse the given stream and drive the given callback
with the results of the parse.

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

Parser

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

parse

​(

Reader

r,

HTMLEditorKit.ParserCallback

cb,
boolean ignoreCharSet)

Parse the given stream and drive the given callback
with the results of the parse.

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

Parse the given stream and drive the given callback
with the results of the parse.

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

- Parser

```java
public Parser()
```

============ METHOD DETAIL ==========

- Method Detail

- parse

```java
public abstract void parse​(
Reader
r,

HTMLEditorKit.ParserCallback
cb,
boolean ignoreCharSet)
throws
IOException
```

Parse the given stream and drive the given callback
with the results of the parse. This method should
be implemented to be thread-safe.

**Parameters:** r

- a reader
**Parameters:** cb

- a parser callback
**Parameters:** ignoreCharSet

- if

true

charset is ignoring
**Throws:** IOException

- if an I/O exception occurs

Constructor Detail

- Parser

```java
public Parser()
```

---

#### Constructor Detail

Parser

```java
public Parser()
```

---

#### Parser

public Parser()

Method Detail

- parse

```java
public abstract void parse​(
Reader
r,

HTMLEditorKit.ParserCallback
cb,
boolean ignoreCharSet)
throws
IOException
```

Parse the given stream and drive the given callback
with the results of the parse. This method should
be implemented to be thread-safe.

**Parameters:** r

- a reader
**Parameters:** cb

- a parser callback
**Parameters:** ignoreCharSet

- if

true

charset is ignoring
**Throws:** IOException

- if an I/O exception occurs

---

#### Method Detail

parse

```java
public abstract void parse​(
Reader
r,

HTMLEditorKit.ParserCallback
cb,
boolean ignoreCharSet)
throws
IOException
```

Parse the given stream and drive the given callback
with the results of the parse. This method should
be implemented to be thread-safe.

**Parameters:** r

- a reader
**Parameters:** cb

- a parser callback
**Parameters:** ignoreCharSet

- if

true

charset is ignoring
**Throws:** IOException

- if an I/O exception occurs

---

#### parse

public abstract void parse​(

Reader

r,

HTMLEditorKit.ParserCallback

cb,
boolean ignoreCharSet)
throws

IOException

Parse the given stream and drive the given callback
with the results of the parse. This method should
be implemented to be thread-safe.

---

