# Interface BeanContextProxy

**Source:** `java.desktop\java\beans\beancontext\BeanContextProxy.html`

### Class Description

```java
public interface
BeanContextProxy
```

This interface is implemented by a JavaBean that does
not directly have a BeanContext(Child) associated with
it (via implementing that interface or a subinterface thereof),
but has a public BeanContext(Child) delegated from it.
For example, a subclass of java.awt.Container may have a BeanContext
associated with it that all Component children of that Container shall
be contained within.

An Object may not implement this interface and the
BeanContextChild interface
(or any subinterfaces thereof) they are mutually exclusive.

Callers of this interface shall examine the return type in order to
obtain a particular subinterface of BeanContextChild as follows:

```java
BeanContextChild bcc = o.getBeanContextProxy();

if (bcc instanceof BeanContext) {
// ...
}
```

or

```java
BeanContextChild bcc = o.getBeanContextProxy();
BeanContext bc = null;

try {
bc = (BeanContext)bcc;
} catch (ClassCastException cce) {
// cast failed, bcc is not an instanceof BeanContext
}
```

The return value is a constant for the lifetime of the implementing
instance

**Since:** 1.2
**See Also:** BeanContextChild

,

BeanContextChildSupport

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### BeanContextChild
getBeanContextProxy()

Gets the

BeanContextChild

(or subinterface)
associated with this object.

**Returns:**
- the

BeanContextChild

(or subinterface)
associated with this object

---

### Additional Sections

#### Interface BeanContextProxy

```java
public interface
BeanContextProxy
```

This interface is implemented by a JavaBean that does
not directly have a BeanContext(Child) associated with
it (via implementing that interface or a subinterface thereof),
but has a public BeanContext(Child) delegated from it.
For example, a subclass of java.awt.Container may have a BeanContext
associated with it that all Component children of that Container shall
be contained within.

An Object may not implement this interface and the
BeanContextChild interface
(or any subinterfaces thereof) they are mutually exclusive.

Callers of this interface shall examine the return type in order to
obtain a particular subinterface of BeanContextChild as follows:

```java
BeanContextChild bcc = o.getBeanContextProxy();

if (bcc instanceof BeanContext) {
// ...
}
```

or

```java
BeanContextChild bcc = o.getBeanContextProxy();
BeanContext bc = null;

try {
bc = (BeanContext)bcc;
} catch (ClassCastException cce) {
// cast failed, bcc is not an instanceof BeanContext
}
```

The return value is a constant for the lifetime of the implementing
instance

**Since:** 1.2
**See Also:** BeanContextChild

,

BeanContextChildSupport

public interface

BeanContextProxy

This interface is implemented by a JavaBean that does
not directly have a BeanContext(Child) associated with
it (via implementing that interface or a subinterface thereof),
but has a public BeanContext(Child) delegated from it.
For example, a subclass of java.awt.Container may have a BeanContext
associated with it that all Component children of that Container shall
be contained within.

An Object may not implement this interface and the
BeanContextChild interface
(or any subinterfaces thereof) they are mutually exclusive.

Callers of this interface shall examine the return type in order to
obtain a particular subinterface of BeanContextChild as follows:

```java
BeanContextChild bcc = o.getBeanContextProxy();

if (bcc instanceof BeanContext) {
// ...
}
```

or

```java
BeanContextChild bcc = o.getBeanContextProxy();
BeanContext bc = null;

try {
bc = (BeanContext)bcc;
} catch (ClassCastException cce) {
// cast failed, bcc is not an instanceof BeanContext
}
```

The return value is a constant for the lifetime of the implementing
instance

This interface is implemented by a JavaBean that does
not directly have a BeanContext(Child) associated with
it (via implementing that interface or a subinterface thereof),
but has a public BeanContext(Child) delegated from it.
For example, a subclass of java.awt.Container may have a BeanContext
associated with it that all Component children of that Container shall
be contained within.

An Object may not implement this interface and the
BeanContextChild interface
(or any subinterfaces thereof) they are mutually exclusive.

Callers of this interface shall examine the return type in order to
obtain a particular subinterface of BeanContextChild as follows:

```java
BeanContextChild bcc = o.getBeanContextProxy();

if (bcc instanceof BeanContext) {
// ...
}
```

or

```java
BeanContextChild bcc = o.getBeanContextProxy();
BeanContext bc = null;

try {
bc = (BeanContext)bcc;
} catch (ClassCastException cce) {
// cast failed, bcc is not an instanceof BeanContext
}
```

The return value is a constant for the lifetime of the implementing
instance

BeanContextChild bcc = o.getBeanContextProxy();

if (bcc instanceof BeanContext) {
// ...
}

BeanContextChild bcc = o.getBeanContextProxy();
BeanContext bc = null;

try {
bc = (BeanContext)bcc;
} catch (ClassCastException cce) {
// cast failed, bcc is not an instanceof BeanContext
}

The return value is a constant for the lifetime of the implementing
instance

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BeanContextChild

getBeanContextProxy

()

Gets the

BeanContextChild

(or subinterface)
associated with this object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BeanContextChild

getBeanContextProxy

()

Gets the

BeanContextChild

(or subinterface)
associated with this object.

---

#### Method Summary

Gets the

BeanContextChild

(or subinterface)
associated with this object.

============ METHOD DETAIL ==========

- Method Detail

- getBeanContextProxy

```java
BeanContextChild
getBeanContextProxy()
```

Gets the

BeanContextChild

(or subinterface)
associated with this object.

**Returns:** the

BeanContextChild

(or subinterface)
associated with this object

Method Detail

- getBeanContextProxy

```java
BeanContextChild
getBeanContextProxy()
```

Gets the

BeanContextChild

(or subinterface)
associated with this object.

**Returns:** the

BeanContextChild

(or subinterface)
associated with this object

---

#### Method Detail

getBeanContextProxy

```java
BeanContextChild
getBeanContextProxy()
```

Gets the

BeanContextChild

(or subinterface)
associated with this object.

**Returns:** the

BeanContextChild

(or subinterface)
associated with this object

---

#### getBeanContextProxy

BeanContextChild

getBeanContextProxy()

Gets the

BeanContextChild

(or subinterface)
associated with this object.

---

