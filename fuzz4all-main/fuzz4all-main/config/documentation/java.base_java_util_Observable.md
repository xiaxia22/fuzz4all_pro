# Class Observable

**Source:** `java.base\java\util\Observable.html`

### Class Description

```java
@Deprecated
(
since
="9")
public class
Observable

extends
Object
```

This class represents an observable object, or "data"
in the model-view paradigm. It can be subclassed to represent an
object that the application wants to have observed.

An observable object can have one or more observers. An observer
may be any object that implements interface

Observer

. After an
observable instance changes, an application calling the

Observable

's

notifyObservers

method
causes all of its observers to be notified of the change by a call
to their

update

method.

The order in which notifications will be delivered is unspecified.
The default implementation provided in the Observable class will
notify Observers in the order in which they registered interest, but
subclasses may change this order, use no guaranteed order, deliver
notifications on separate threads, or may guarantee that their
subclass follows this order, as they choose.

Note that this notification mechanism has nothing to do with threads
and is completely separate from the

wait

and

notify

mechanism of class

Object

.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

**Since:** 1.0
**See Also:** notifyObservers()

,

notifyObservers(java.lang.Object)

,

Observer

,

Observer.update(java.util.Observable, java.lang.Object)

---

### Field Details

*No entries found.*

### Constructor Details

#### public Observable()

Construct an Observable with zero Observers.

---

### Method Details

#### public void addObserver​(
Observer
o)

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.
The order in which notifications will be delivered to multiple
observers is not specified. See the class comment.

**Parameters:**
- o

- an observer to be added.

**Throws:**
- NullPointerException

- if the parameter o is null.

---

#### public void deleteObserver​(
Observer
o)

Deletes an observer from the set of observers of this object.
Passing

null

to this method will have no effect.

**Parameters:**
- o

- the observer to be deleted.

---

#### public void notifyObservers()

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and

null

. In other
words, this method is equivalent to:

notifyObservers(null)

**See Also:**
- clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

---

#### public void notifyObservers​(
Object
arg)

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and the

arg

argument.

**Parameters:**
- arg

- any object.

**See Also:**
- clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

---

#### public void deleteObservers()

Clears the observer list so that this object no longer has any observers.

---

#### protected void setChanged()

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

---

#### protected void clearChanged()

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.
This method is called automatically by the

notifyObservers

methods.

**See Also:**
- notifyObservers()

,

notifyObservers(java.lang.Object)

---

#### public boolean hasChanged()

Tests if this object has changed.

**Returns:**
- true

if and only if the

setChanged

method has been called more recently than the

clearChanged

method on this object;

false

otherwise.

**See Also:**
- clearChanged()

,

setChanged()

---

#### public int countObservers()

Returns the number of observers of this

Observable

object.

**Returns:**
- the number of observers of this object.

---

### Additional Sections

#### Class Observable

java.lang.Object

- java.util.Observable

java.util.Observable

```java
@Deprecated
(
since
="9")
public class
Observable

extends
Object
```

Deprecated.

This class and the

Observer

interface have been deprecated.
The event model supported by

Observer

and

Observable

is quite limited, the order of notifications delivered by

Observable

is unspecified, and state changes are not in
one-for-one correspondence with notifications.
For a richer event model, consider using the

java.beans

package. For reliable and ordered
messaging among threads, consider using one of the concurrent data
structures in the

java.util.concurrent

package.
For reactive streams style programming, see the

Flow

API.

This class represents an observable object, or "data"
in the model-view paradigm. It can be subclassed to represent an
object that the application wants to have observed.

An observable object can have one or more observers. An observer
may be any object that implements interface

Observer

. After an
observable instance changes, an application calling the

Observable

's

notifyObservers

method
causes all of its observers to be notified of the change by a call
to their

update

method.

The order in which notifications will be delivered is unspecified.
The default implementation provided in the Observable class will
notify Observers in the order in which they registered interest, but
subclasses may change this order, use no guaranteed order, deliver
notifications on separate threads, or may guarantee that their
subclass follows this order, as they choose.

Note that this notification mechanism has nothing to do with threads
and is completely separate from the

wait

and

notify

mechanism of class

Object

.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

**Since:** 1.0
**See Also:** notifyObservers()

,

notifyObservers(java.lang.Object)

,

Observer

,

Observer.update(java.util.Observable, java.lang.Object)

@Deprecated

(

since

="9")
public class

Observable

extends

Object

This class represents an observable object, or "data"
in the model-view paradigm. It can be subclassed to represent an
object that the application wants to have observed.

An observable object can have one or more observers. An observer
may be any object that implements interface

Observer

. After an
observable instance changes, an application calling the

Observable

's

notifyObservers

method
causes all of its observers to be notified of the change by a call
to their

update

method.

The order in which notifications will be delivered is unspecified.
The default implementation provided in the Observable class will
notify Observers in the order in which they registered interest, but
subclasses may change this order, use no guaranteed order, deliver
notifications on separate threads, or may guarantee that their
subclass follows this order, as they choose.

Note that this notification mechanism has nothing to do with threads
and is completely separate from the

wait

and

notify

mechanism of class

Object

.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

An observable object can have one or more observers. An observer
may be any object that implements interface

Observer

. After an
observable instance changes, an application calling the

Observable

's

notifyObservers

method
causes all of its observers to be notified of the change by a call
to their

update

method.

The order in which notifications will be delivered is unspecified.
The default implementation provided in the Observable class will
notify Observers in the order in which they registered interest, but
subclasses may change this order, use no guaranteed order, deliver
notifications on separate threads, or may guarantee that their
subclass follows this order, as they choose.

Note that this notification mechanism has nothing to do with threads
and is completely separate from the

wait

and

notify

mechanism of class

Object

.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

The order in which notifications will be delivered is unspecified.
The default implementation provided in the Observable class will
notify Observers in the order in which they registered interest, but
subclasses may change this order, use no guaranteed order, deliver
notifications on separate threads, or may guarantee that their
subclass follows this order, as they choose.

Note that this notification mechanism has nothing to do with threads
and is completely separate from the

wait

and

notify

mechanism of class

Object

.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

Note that this notification mechanism has nothing to do with threads
and is completely separate from the

wait

and

notify

mechanism of class

Object

.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

When an observable object is newly created, its set of observers is
empty. Two observers are considered the same if and only if the

equals

method returns true for them.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Observable

()

Deprecated.

Construct an Observable with zero Observers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addObserver

​(

Observer

o)

Deprecated.

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.

protected void

clearChanged

()

Deprecated.

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.

int

countObservers

()

Deprecated.

Returns the number of observers of this

Observable

object.

void

deleteObserver

​(

Observer

o)

Deprecated.

Deletes an observer from the set of observers of this object.

void

deleteObservers

()

Deprecated.

Clears the observer list so that this object no longer has any observers.

boolean

hasChanged

()

Deprecated.

Tests if this object has changed.

void

notifyObservers

()

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

void

notifyObservers

​(

Object

arg)

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

protected void

setChanged

()

Deprecated.

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

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

Observable

()

Deprecated.

Construct an Observable with zero Observers.

---

#### Constructor Summary

Deprecated.

Construct an Observable with zero Observers.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addObserver

​(

Observer

o)

Deprecated.

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.

protected void

clearChanged

()

Deprecated.

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.

int

countObservers

()

Deprecated.

Returns the number of observers of this

Observable

object.

void

deleteObserver

​(

Observer

o)

Deprecated.

Deletes an observer from the set of observers of this object.

void

deleteObservers

()

Deprecated.

Clears the observer list so that this object no longer has any observers.

boolean

hasChanged

()

Deprecated.

Tests if this object has changed.

void

notifyObservers

()

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

void

notifyObservers

​(

Object

arg)

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

protected void

setChanged

()

Deprecated.

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

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

Deprecated.

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.

Returns the number of observers of this

Observable

object.

Deletes an observer from the set of observers of this object.

Clears the observer list so that this object no longer has any observers.

Tests if this object has changed.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

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

- Observable

```java
public Observable()
```

Deprecated.

Construct an Observable with zero Observers.

============ METHOD DETAIL ==========

- Method Detail

- addObserver

```java
public void addObserver​(
Observer
o)
```

Deprecated.

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.
The order in which notifications will be delivered to multiple
observers is not specified. See the class comment.

**Parameters:** o

- an observer to be added.
**Throws:** NullPointerException

- if the parameter o is null.

- deleteObserver

```java
public void deleteObserver​(
Observer
o)
```

Deprecated.

Deletes an observer from the set of observers of this object.
Passing

null

to this method will have no effect.

**Parameters:** o

- the observer to be deleted.

- notifyObservers

```java
public void notifyObservers()
```

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and

null

. In other
words, this method is equivalent to:

notifyObservers(null)

**See Also:** clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

- notifyObservers

```java
public void notifyObservers​(
Object
arg)
```

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and the

arg

argument.

**Parameters:** arg

- any object.
**See Also:** clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

- deleteObservers

```java
public void deleteObservers()
```

Deprecated.

Clears the observer list so that this object no longer has any observers.

- setChanged

```java
protected void setChanged()
```

Deprecated.

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

- clearChanged

```java
protected void clearChanged()
```

Deprecated.

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.
This method is called automatically by the

notifyObservers

methods.

**See Also:** notifyObservers()

,

notifyObservers(java.lang.Object)

- hasChanged

```java
public boolean hasChanged()
```

Deprecated.

Tests if this object has changed.

**Returns:** true

if and only if the

setChanged

method has been called more recently than the

clearChanged

method on this object;

false

otherwise.
**See Also:** clearChanged()

,

setChanged()

- countObservers

```java
public int countObservers()
```

Deprecated.

Returns the number of observers of this

Observable

object.

**Returns:** the number of observers of this object.

Constructor Detail

- Observable

```java
public Observable()
```

Deprecated.

Construct an Observable with zero Observers.

---

#### Constructor Detail

Observable

```java
public Observable()
```

Deprecated.

Construct an Observable with zero Observers.

---

#### Observable

public Observable()

Construct an Observable with zero Observers.

Method Detail

- addObserver

```java
public void addObserver​(
Observer
o)
```

Deprecated.

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.
The order in which notifications will be delivered to multiple
observers is not specified. See the class comment.

**Parameters:** o

- an observer to be added.
**Throws:** NullPointerException

- if the parameter o is null.

- deleteObserver

```java
public void deleteObserver​(
Observer
o)
```

Deprecated.

Deletes an observer from the set of observers of this object.
Passing

null

to this method will have no effect.

**Parameters:** o

- the observer to be deleted.

- notifyObservers

```java
public void notifyObservers()
```

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and

null

. In other
words, this method is equivalent to:

notifyObservers(null)

**See Also:** clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

- notifyObservers

```java
public void notifyObservers​(
Object
arg)
```

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and the

arg

argument.

**Parameters:** arg

- any object.
**See Also:** clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

- deleteObservers

```java
public void deleteObservers()
```

Deprecated.

Clears the observer list so that this object no longer has any observers.

- setChanged

```java
protected void setChanged()
```

Deprecated.

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

- clearChanged

```java
protected void clearChanged()
```

Deprecated.

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.
This method is called automatically by the

notifyObservers

methods.

**See Also:** notifyObservers()

,

notifyObservers(java.lang.Object)

- hasChanged

```java
public boolean hasChanged()
```

Deprecated.

Tests if this object has changed.

**Returns:** true

if and only if the

setChanged

method has been called more recently than the

clearChanged

method on this object;

false

otherwise.
**See Also:** clearChanged()

,

setChanged()

- countObservers

```java
public int countObservers()
```

Deprecated.

Returns the number of observers of this

Observable

object.

**Returns:** the number of observers of this object.

---

#### Method Detail

addObserver

```java
public void addObserver​(
Observer
o)
```

Deprecated.

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.
The order in which notifications will be delivered to multiple
observers is not specified. See the class comment.

**Parameters:** o

- an observer to be added.
**Throws:** NullPointerException

- if the parameter o is null.

---

#### addObserver

public void addObserver​(

Observer

o)

Adds an observer to the set of observers for this object, provided
that it is not the same as some observer already in the set.
The order in which notifications will be delivered to multiple
observers is not specified. See the class comment.

deleteObserver

```java
public void deleteObserver​(
Observer
o)
```

Deprecated.

Deletes an observer from the set of observers of this object.
Passing

null

to this method will have no effect.

**Parameters:** o

- the observer to be deleted.

---

#### deleteObserver

public void deleteObserver​(

Observer

o)

Deletes an observer from the set of observers of this object.
Passing

null

to this method will have no effect.

notifyObservers

```java
public void notifyObservers()
```

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and

null

. In other
words, this method is equivalent to:

notifyObservers(null)

**See Also:** clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

---

#### notifyObservers

public void notifyObservers()

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to
indicate that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and

null

. In other
words, this method is equivalent to:

notifyObservers(null)

Each observer has its

update

method called with two
arguments: this observable object and

null

. In other
words, this method is equivalent to:

notifyObservers(null)

notifyObservers

```java
public void notifyObservers​(
Object
arg)
```

Deprecated.

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and the

arg

argument.

**Parameters:** arg

- any object.
**See Also:** clearChanged()

,

hasChanged()

,

Observer.update(java.util.Observable, java.lang.Object)

---

#### notifyObservers

public void notifyObservers​(

Object

arg)

If this object has changed, as indicated by the

hasChanged

method, then notify all of its observers
and then call the

clearChanged

method to indicate
that this object has no longer changed.

Each observer has its

update

method called with two
arguments: this observable object and the

arg

argument.

Each observer has its

update

method called with two
arguments: this observable object and the

arg

argument.

deleteObservers

```java
public void deleteObservers()
```

Deprecated.

Clears the observer list so that this object no longer has any observers.

---

#### deleteObservers

public void deleteObservers()

Clears the observer list so that this object no longer has any observers.

setChanged

```java
protected void setChanged()
```

Deprecated.

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

---

#### setChanged

protected void setChanged()

Marks this

Observable

object as having been changed; the

hasChanged

method will now return

true

.

clearChanged

```java
protected void clearChanged()
```

Deprecated.

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.
This method is called automatically by the

notifyObservers

methods.

**See Also:** notifyObservers()

,

notifyObservers(java.lang.Object)

---

#### clearChanged

protected void clearChanged()

Indicates that this object has no longer changed, or that it has
already notified all of its observers of its most recent change,
so that the

hasChanged

method will now return

false

.
This method is called automatically by the

notifyObservers

methods.

hasChanged

```java
public boolean hasChanged()
```

Deprecated.

Tests if this object has changed.

**Returns:** true

if and only if the

setChanged

method has been called more recently than the

clearChanged

method on this object;

false

otherwise.
**See Also:** clearChanged()

,

setChanged()

---

#### hasChanged

public boolean hasChanged()

Tests if this object has changed.

countObservers

```java
public int countObservers()
```

Deprecated.

Returns the number of observers of this

Observable

object.

**Returns:** the number of observers of this object.

---

#### countObservers

public int countObservers()

Returns the number of observers of this

Observable

object.

---

