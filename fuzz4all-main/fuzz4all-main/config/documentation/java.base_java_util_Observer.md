# Interface Observer

**Source:** `java.base\java\util\Observer.html`

### Class Description

```java
@Deprecated
(
since
="9")
public interface
Observer
```

A class can implement the

Observer

interface when it
wants to be informed of changes in observable objects.

**Since:** 1.0
**See Also:** Observable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void update​(
Observable
o,

Object
arg)

This method is called whenever the observed object is changed. An
application calls an

Observable

object's

notifyObservers

method to have all the object's
observers notified of the change.

**Parameters:**
- o

- the observable object.
- arg

- an argument passed to the

notifyObservers

method.

---

### Additional Sections

#### Interface Observer

```java
@Deprecated
(
since
="9")
public interface
Observer
```

Deprecated.

This interface has been deprecated. See the

Observable

class for further information.

A class can implement the

Observer

interface when it
wants to be informed of changes in observable objects.

**Since:** 1.0
**See Also:** Observable

@Deprecated

(

since

="9")
public interface

Observer

A class can implement the

Observer

interface when it
wants to be informed of changes in observable objects.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

update

​(

Observable

o,

Object

arg)

Deprecated.

This method is called whenever the observed object is changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

update

​(

Observable

o,

Object

arg)

Deprecated.

This method is called whenever the observed object is changed.

---

#### Method Summary

Deprecated.

This method is called whenever the observed object is changed.

============ METHOD DETAIL ==========

- Method Detail

- update

```java
void update​(
Observable
o,

Object
arg)
```

Deprecated.

This method is called whenever the observed object is changed. An
application calls an

Observable

object's

notifyObservers

method to have all the object's
observers notified of the change.

**Parameters:** o

- the observable object.
**Parameters:** arg

- an argument passed to the

notifyObservers

method.

Method Detail

- update

```java
void update​(
Observable
o,

Object
arg)
```

Deprecated.

This method is called whenever the observed object is changed. An
application calls an

Observable

object's

notifyObservers

method to have all the object's
observers notified of the change.

**Parameters:** o

- the observable object.
**Parameters:** arg

- an argument passed to the

notifyObservers

method.

---

#### Method Detail

update

```java
void update​(
Observable
o,

Object
arg)
```

Deprecated.

This method is called whenever the observed object is changed. An
application calls an

Observable

object's

notifyObservers

method to have all the object's
observers notified of the change.

**Parameters:** o

- the observable object.
**Parameters:** arg

- an argument passed to the

notifyObservers

method.

---

#### update

void update​(

Observable

o,

Object

arg)

This method is called whenever the observed object is changed. An
application calls an

Observable

object's

notifyObservers

method to have all the object's
observers notified of the change.

---

