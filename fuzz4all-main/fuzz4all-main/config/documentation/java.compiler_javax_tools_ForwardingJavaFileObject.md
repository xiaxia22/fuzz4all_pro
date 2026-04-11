# Class ForwardingJavaFileObject<F extends JavaFileObject >

**Source:** `java.compiler\javax\tools\ForwardingJavaFileObject.html`

### Class Description

```java
public class
ForwardingJavaFileObject<F extends
JavaFileObject
>

extends
ForwardingFileObject
<F>
implements
JavaFileObject
```

Forwards calls to a given file object. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

**Type Parameters:** F

- the kind of file object forwarded to by this object

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ForwardingJavaFileObject​(
F
fileObject)

Creates a new instance of ForwardingJavaFileObject.

**Parameters:**
- fileObject

- delegate to this file object

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ForwardingJavaFileObject<F extends JavaFileObject >

java.lang.Object

- javax.tools.ForwardingFileObject

<F>
- - javax.tools.ForwardingJavaFileObject<F>

javax.tools.ForwardingFileObject

<F>

- javax.tools.ForwardingJavaFileObject<F>

javax.tools.ForwardingJavaFileObject<F>

**Type Parameters:** F

- the kind of file object forwarded to by this object

**All Implemented Interfaces:** FileObject

,

JavaFileObject

```java
public class
ForwardingJavaFileObject<F extends
JavaFileObject
>

extends
ForwardingFileObject
<F>
implements
JavaFileObject
```

Forwards calls to a given file object. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

**Since:** 1.6

public class

ForwardingJavaFileObject<F extends

JavaFileObject

>

extends

ForwardingFileObject

<F>
implements

JavaFileObject

Forwards calls to a given file object. Subclasses of this class
might override some of these methods and might also provide
additional fields and methods.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface javax.tools.

JavaFileObject

JavaFileObject.Kind

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.tools.

ForwardingFileObject

fileObject

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForwardingJavaFileObject

​(

F

fileObject)

Creates a new instance of ForwardingJavaFileObject.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.tools.

ForwardingFileObject

getCharContent

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

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

- Methods declared in interface javax.tools.

FileObject

delete

,

getCharContent

,

getLastModified

,

getName

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

,

toUri

- Methods declared in interface javax.tools.

JavaFileObject

getAccessLevel

,

getKind

,

getNestingKind

,

isNameCompatible

Nested Class Summary

- Nested classes/interfaces declared in interface javax.tools.

JavaFileObject

JavaFileObject.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface javax.tools.

JavaFileObject

JavaFileObject.Kind

---

#### Nested classes/interfaces declared in interface javax.tools. JavaFileObject

Field Summary

- Fields declared in class javax.tools.

ForwardingFileObject

fileObject

---

#### Field Summary

Fields declared in class javax.tools.

ForwardingFileObject

fileObject

---

#### Fields declared in class javax.tools. ForwardingFileObject

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ForwardingJavaFileObject

​(

F

fileObject)

Creates a new instance of ForwardingJavaFileObject.

---

#### Constructor Summary

Creates a new instance of ForwardingJavaFileObject.

Method Summary

- Methods declared in class javax.tools.

ForwardingFileObject

getCharContent

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

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

- Methods declared in interface javax.tools.

FileObject

delete

,

getCharContent

,

getLastModified

,

getName

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

,

toUri

- Methods declared in interface javax.tools.

JavaFileObject

getAccessLevel

,

getKind

,

getNestingKind

,

isNameCompatible

---

#### Method Summary

Methods declared in class javax.tools.

ForwardingFileObject

getCharContent

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

---

#### Methods declared in class javax.tools. ForwardingFileObject

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

Methods declared in interface javax.tools.

FileObject

delete

,

getCharContent

,

getLastModified

,

getName

,

openInputStream

,

openOutputStream

,

openReader

,

openWriter

,

toUri

---

#### Methods declared in interface javax.tools. FileObject

Methods declared in interface javax.tools.

JavaFileObject

getAccessLevel

,

getKind

,

getNestingKind

,

isNameCompatible

---

#### Methods declared in interface javax.tools. JavaFileObject

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ForwardingJavaFileObject

```java
protected ForwardingJavaFileObject​(
F
fileObject)
```

Creates a new instance of ForwardingJavaFileObject.

**Parameters:** fileObject

- delegate to this file object

Constructor Detail

- ForwardingJavaFileObject

```java
protected ForwardingJavaFileObject​(
F
fileObject)
```

Creates a new instance of ForwardingJavaFileObject.

**Parameters:** fileObject

- delegate to this file object

---

#### Constructor Detail

ForwardingJavaFileObject

```java
protected ForwardingJavaFileObject​(
F
fileObject)
```

Creates a new instance of ForwardingJavaFileObject.

**Parameters:** fileObject

- delegate to this file object

---

#### ForwardingJavaFileObject

protected ForwardingJavaFileObject​(

F

fileObject)

Creates a new instance of ForwardingJavaFileObject.

---

