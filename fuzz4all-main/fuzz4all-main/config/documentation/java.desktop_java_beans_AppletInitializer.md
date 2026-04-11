# Interface AppletInitializer

**Source:** `java.desktop\java\beans\AppletInitializer.html`

### Class Description

```java
@Deprecated
(
since
="9")
public interface
AppletInitializer
```

This interface is designed to work in collusion with java.beans.Beans.instantiate.
The interface is intended to provide mechanism to allow the proper
initialization of JavaBeans that are also Applets, during their
instantiation by java.beans.Beans.instantiate().

**Since:** 1.2
**See Also:** Beans.instantiate(java.lang.ClassLoader, java.lang.String)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void initialize​(
Applet
newAppletBean,

BeanContext
bCtxt)

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Conformant implementations shall:

- Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

**Parameters:**
- newAppletBean

- The newly instantiated JavaBean
- bCtxt

- The BeanContext intended for this Applet, or
null.

---

#### void activate​(
Applet
newApplet)

Activate, and/or mark Applet active. Implementors of this interface
shall mark this Applet as active, and optionally invoke its start()
method.

**Parameters:**
- newApplet

- The newly instantiated JavaBean

---

### Additional Sections

#### Interface AppletInitializer

```java
@Deprecated
(
since
="9")
public interface
AppletInitializer
```

Deprecated.

The Applet API is deprecated. See the

java.applet package
documentation

for further information.

This interface is designed to work in collusion with java.beans.Beans.instantiate.
The interface is intended to provide mechanism to allow the proper
initialization of JavaBeans that are also Applets, during their
instantiation by java.beans.Beans.instantiate().

**Since:** 1.2
**See Also:** Beans.instantiate(java.lang.ClassLoader, java.lang.String)

@Deprecated

(

since

="9")
public interface

AppletInitializer

This interface is designed to work in collusion with java.beans.Beans.instantiate.
The interface is intended to provide mechanism to allow the proper
initialization of JavaBeans that are also Applets, during their
instantiation by java.beans.Beans.instantiate().

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

activate

​(

Applet

newApplet)

Deprecated.

Activate, and/or mark Applet active.

void

initialize

​(

Applet

newAppletBean,

BeanContext

bCtxt)

Deprecated.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

activate

​(

Applet

newApplet)

Deprecated.

Activate, and/or mark Applet active.

void

initialize

​(

Applet

newAppletBean,

BeanContext

bCtxt)

Deprecated.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

---

#### Method Summary

Deprecated.

Activate, and/or mark Applet active.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

============ METHOD DETAIL ==========

- Method Detail

- initialize

```java
void initialize​(
Applet
newAppletBean,

BeanContext
bCtxt)
```

Deprecated.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Conformant implementations shall:

- Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

**Parameters:** newAppletBean

- The newly instantiated JavaBean
**Parameters:** bCtxt

- The BeanContext intended for this Applet, or
null.

- activate

```java
void activate​(
Applet
newApplet)
```

Deprecated.

Activate, and/or mark Applet active. Implementors of this interface
shall mark this Applet as active, and optionally invoke its start()
method.

**Parameters:** newApplet

- The newly instantiated JavaBean

Method Detail

- initialize

```java
void initialize​(
Applet
newAppletBean,

BeanContext
bCtxt)
```

Deprecated.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Conformant implementations shall:

- Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

**Parameters:** newAppletBean

- The newly instantiated JavaBean
**Parameters:** bCtxt

- The BeanContext intended for this Applet, or
null.

- activate

```java
void activate​(
Applet
newApplet)
```

Deprecated.

Activate, and/or mark Applet active. Implementors of this interface
shall mark this Applet as active, and optionally invoke its start()
method.

**Parameters:** newApplet

- The newly instantiated JavaBean

---

#### Method Detail

initialize

```java
void initialize​(
Applet
newAppletBean,

BeanContext
bCtxt)
```

Deprecated.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Conformant implementations shall:

- Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

**Parameters:** newAppletBean

- The newly instantiated JavaBean
**Parameters:** bCtxt

- The BeanContext intended for this Applet, or
null.

---

#### initialize

void initialize​(

Applet

newAppletBean,

BeanContext

bCtxt)

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Conformant implementations shall:

- Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

If passed to the appropriate variant of java.beans.Beans.instantiate
this method will be called in order to associate the newly instantiated
Applet (JavaBean) with its AppletContext, AppletStub, and Container.

Conformant implementations shall:

- Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

Associate the newly instantiated Applet with the appropriate
AppletContext.

Instantiate an AppletStub() and associate that AppletStub with
the Applet via an invocation of setStub().

If BeanContext parameter is null, then it shall associate the
Applet with its appropriate Container by adding that Applet to its
Container via an invocation of add(). If the BeanContext parameter is
non-null, then it is the responsibility of the BeanContext to associate
the Applet with its Container during the subsequent invocation of its
addChildren() method.

activate

```java
void activate​(
Applet
newApplet)
```

Deprecated.

Activate, and/or mark Applet active. Implementors of this interface
shall mark this Applet as active, and optionally invoke its start()
method.

**Parameters:** newApplet

- The newly instantiated JavaBean

---

#### activate

void activate​(

Applet

newApplet)

Activate, and/or mark Applet active. Implementors of this interface
shall mark this Applet as active, and optionally invoke its start()
method.

---

