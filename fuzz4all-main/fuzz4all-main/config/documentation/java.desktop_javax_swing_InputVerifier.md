# Class InputVerifier

**Source:** `java.desktop\javax\swing\InputVerifier.html`

### Class Description

```java
public abstract class
InputVerifier

extends
Object
```

This class provides the validation mechanism for Swing components. GUIs often
need to ensure that the components are in a valid state before allowing the
user to navigate the input focus. To do this, clients create a subclass of

InputVerifier

and, using

JComponent

's

setInputVerifier

method, attach an instance of their subclass to
the

JComponent

which is the source of the focus transfer operation.
The

InputVerifier

also provides the possibility to validate against
the target of the focus transfer which may reject the focus.
Before focus is transferred from the source Swing component to the target
Swing component, the input verifier's

shouldYieldFocus(source, target)

method is called. Focus is
transferred only if that method returns

true

.

The following example has two text fields, with the first one expecting
the string "pass" to be entered by the user. If either that string is entered
in the first text field or the second text field contains "accept" string,
then the user can advance focus to the second text field by clicking in it or
by pressing TAB.
However, if another string is entered in the first text field and the second
text field does not contain "accept", then the user will be unable to
transfer focus to the second text field.

```java
import java.awt.*;
import javax.swing.*;

// This program demonstrates the use of the Swing InputVerifier class.
// It creates two text fields; the first of the text fields expects the
// string "pass" as input, and will allow focus to advance to the second text
// field if either that string is typed in by the user or the second
// field contains "accept" string.

public class VerifierTest extends JFrame {

public VerifierTest() {
JTextField field1 = new JTextField("Type \"pass\" here");
JTextField field2 = new JTextField("or \"accept\" here");
getContentPane().add(field1, BorderLayout.NORTH);
getContentPane().add(field2, BorderLayout.SOUTH);

field.setInputVerifier(new InputVerifier() {
public boolean verify(JComponent input) {
return "pass".equals(((JTextField) input).getText());
}

public boolean verifyTarget(JComponent input) {
return "accept".equals(((JTextField) input).getText());
}

public boolean shouldYieldFocus(JComponent source,
JComponent target) {
return verify(source) || verifyTarget(target);
}
});

pack();
setVisible(true);
}

public static void main(String[] args) {
SwingUtilities.invokeLater(VerifierTest::new);
}
}
```

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

#### public InputVerifier()

*No description found.*

---

### Method Details

#### public abstract boolean verify​(
JComponent
input)

Checks whether the JComponent's input is valid. This method should
have no side effects. It returns a boolean indicating the status
of the argument's input.

**Parameters:**
- input

- the JComponent to verify

**Returns:**
- true

when valid,

false

when invalid

**See Also:**
- JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### @Deprecated
(
since
="9")
public boolean shouldYieldFocus​(
JComponent
input)

Calls

verify(input)

to ensure that the input is valid.
This method can have side effects. In particular, this method
is called when the user attempts to advance focus out of the
argument component into another Swing component in this window.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the argument component.

**Parameters:**
- input

- the JComponent to verify

**Returns:**
- true

when valid,

false

when invalid

**See Also:**
- JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### public boolean verifyTarget​(
JComponent
target)

Checks whether the target JComponent that will be receiving the focus
is ready to accept it. This method should be over-ridden only if it is
necessary to validate the target of the focus transfer.
This method should have no side effects. It returns a boolean
indicating the status of the argument's input.

**Parameters:**
- target

- the target JComponent to verify

**Returns:**
- true

when valid,

false

when invalid

**See Also:**
- JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

**Since:**
- 9

**Implementation Requirements:**
- By default this method returns

true

.

---

#### public boolean shouldYieldFocus​(
JComponent
source,

JComponent
target)

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.
This method can have side effects.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the first argument component.

**Parameters:**
- source

- the source JComponent of the focus transfer
- target

- the target JComponent of the focus transfer

**Returns:**
- true

when valid,

false

when invalid

**See Also:**
- JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

**Since:**
- 9

**Implementation Requirements:**
- The basic implementation of this method returns the conjunction
of results obtained from

verify(input)

and

verifyTarget(input)

to ensure that both the source and the target
components are in valid state.

---

### Additional Sections

#### Class InputVerifier

java.lang.Object

- javax.swing.InputVerifier

javax.swing.InputVerifier

```java
public abstract class
InputVerifier

extends
Object
```

This class provides the validation mechanism for Swing components. GUIs often
need to ensure that the components are in a valid state before allowing the
user to navigate the input focus. To do this, clients create a subclass of

InputVerifier

and, using

JComponent

's

setInputVerifier

method, attach an instance of their subclass to
the

JComponent

which is the source of the focus transfer operation.
The

InputVerifier

also provides the possibility to validate against
the target of the focus transfer which may reject the focus.
Before focus is transferred from the source Swing component to the target
Swing component, the input verifier's

shouldYieldFocus(source, target)

method is called. Focus is
transferred only if that method returns

true

.

The following example has two text fields, with the first one expecting
the string "pass" to be entered by the user. If either that string is entered
in the first text field or the second text field contains "accept" string,
then the user can advance focus to the second text field by clicking in it or
by pressing TAB.
However, if another string is entered in the first text field and the second
text field does not contain "accept", then the user will be unable to
transfer focus to the second text field.

```java
import java.awt.*;
import javax.swing.*;

// This program demonstrates the use of the Swing InputVerifier class.
// It creates two text fields; the first of the text fields expects the
// string "pass" as input, and will allow focus to advance to the second text
// field if either that string is typed in by the user or the second
// field contains "accept" string.

public class VerifierTest extends JFrame {

public VerifierTest() {
JTextField field1 = new JTextField("Type \"pass\" here");
JTextField field2 = new JTextField("or \"accept\" here");
getContentPane().add(field1, BorderLayout.NORTH);
getContentPane().add(field2, BorderLayout.SOUTH);

field.setInputVerifier(new InputVerifier() {
public boolean verify(JComponent input) {
return "pass".equals(((JTextField) input).getText());
}

public boolean verifyTarget(JComponent input) {
return "accept".equals(((JTextField) input).getText());
}

public boolean shouldYieldFocus(JComponent source,
JComponent target) {
return verify(source) || verifyTarget(target);
}
});

pack();
setVisible(true);
}

public static void main(String[] args) {
SwingUtilities.invokeLater(VerifierTest::new);
}
}
```

**Since:** 1.3

public abstract class

InputVerifier

extends

Object

This class provides the validation mechanism for Swing components. GUIs often
need to ensure that the components are in a valid state before allowing the
user to navigate the input focus. To do this, clients create a subclass of

InputVerifier

and, using

JComponent

's

setInputVerifier

method, attach an instance of their subclass to
the

JComponent

which is the source of the focus transfer operation.
The

InputVerifier

also provides the possibility to validate against
the target of the focus transfer which may reject the focus.
Before focus is transferred from the source Swing component to the target
Swing component, the input verifier's

shouldYieldFocus(source, target)

method is called. Focus is
transferred only if that method returns

true

.

The following example has two text fields, with the first one expecting
the string "pass" to be entered by the user. If either that string is entered
in the first text field or the second text field contains "accept" string,
then the user can advance focus to the second text field by clicking in it or
by pressing TAB.
However, if another string is entered in the first text field and the second
text field does not contain "accept", then the user will be unable to
transfer focus to the second text field.

```java
import java.awt.*;
import javax.swing.*;

// This program demonstrates the use of the Swing InputVerifier class.
// It creates two text fields; the first of the text fields expects the
// string "pass" as input, and will allow focus to advance to the second text
// field if either that string is typed in by the user or the second
// field contains "accept" string.

public class VerifierTest extends JFrame {

public VerifierTest() {
JTextField field1 = new JTextField("Type \"pass\" here");
JTextField field2 = new JTextField("or \"accept\" here");
getContentPane().add(field1, BorderLayout.NORTH);
getContentPane().add(field2, BorderLayout.SOUTH);

field.setInputVerifier(new InputVerifier() {
public boolean verify(JComponent input) {
return "pass".equals(((JTextField) input).getText());
}

public boolean verifyTarget(JComponent input) {
return "accept".equals(((JTextField) input).getText());
}

public boolean shouldYieldFocus(JComponent source,
JComponent target) {
return verify(source) || verifyTarget(target);
}
});

pack();
setVisible(true);
}

public static void main(String[] args) {
SwingUtilities.invokeLater(VerifierTest::new);
}
}
```

The following example has two text fields, with the first one expecting
the string "pass" to be entered by the user. If either that string is entered
in the first text field or the second text field contains "accept" string,
then the user can advance focus to the second text field by clicking in it or
by pressing TAB.
However, if another string is entered in the first text field and the second
text field does not contain "accept", then the user will be unable to
transfer focus to the second text field.

```java
import java.awt.*;
import javax.swing.*;

// This program demonstrates the use of the Swing InputVerifier class.
// It creates two text fields; the first of the text fields expects the
// string "pass" as input, and will allow focus to advance to the second text
// field if either that string is typed in by the user or the second
// field contains "accept" string.

public class VerifierTest extends JFrame {

public VerifierTest() {
JTextField field1 = new JTextField("Type \"pass\" here");
JTextField field2 = new JTextField("or \"accept\" here");
getContentPane().add(field1, BorderLayout.NORTH);
getContentPane().add(field2, BorderLayout.SOUTH);

field.setInputVerifier(new InputVerifier() {
public boolean verify(JComponent input) {
return "pass".equals(((JTextField) input).getText());
}

public boolean verifyTarget(JComponent input) {
return "accept".equals(((JTextField) input).getText());
}

public boolean shouldYieldFocus(JComponent source,
JComponent target) {
return verify(source) || verifyTarget(target);
}
});

pack();
setVisible(true);
}

public static void main(String[] args) {
SwingUtilities.invokeLater(VerifierTest::new);
}
}
```

import java.awt.*;
import javax.swing.*;

// This program demonstrates the use of the Swing InputVerifier class.
// It creates two text fields; the first of the text fields expects the
// string "pass" as input, and will allow focus to advance to the second text
// field if either that string is typed in by the user or the second
// field contains "accept" string.

public class VerifierTest extends JFrame {

public VerifierTest() {
JTextField field1 = new JTextField("Type \"pass\" here");
JTextField field2 = new JTextField("or \"accept\" here");
getContentPane().add(field1, BorderLayout.NORTH);
getContentPane().add(field2, BorderLayout.SOUTH);

field.setInputVerifier(new InputVerifier() {
public boolean verify(JComponent input) {
return "pass".equals(((JTextField) input).getText());
}

public boolean verifyTarget(JComponent input) {
return "accept".equals(((JTextField) input).getText());
}

public boolean shouldYieldFocus(JComponent source,
JComponent target) {
return verify(source) || verifyTarget(target);
}
});

pack();
setVisible(true);
}

public static void main(String[] args) {
SwingUtilities.invokeLater(VerifierTest::new);
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InputVerifier

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

shouldYieldFocus

​(

JComponent

input)

Deprecated.

use

shouldYieldFocus(JComponent, JComponent)

instead.

boolean

shouldYieldFocus

​(

JComponent

source,

JComponent

target)

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.

abstract boolean

verify

​(

JComponent

input)

Checks whether the JComponent's input is valid.

boolean

verifyTarget

​(

JComponent

target)

Checks whether the target JComponent that will be receiving the focus
is ready to accept it.

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

InputVerifier

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

boolean

shouldYieldFocus

​(

JComponent

input)

Deprecated.

use

shouldYieldFocus(JComponent, JComponent)

instead.

boolean

shouldYieldFocus

​(

JComponent

source,

JComponent

target)

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.

abstract boolean

verify

​(

JComponent

input)

Checks whether the JComponent's input is valid.

boolean

verifyTarget

​(

JComponent

target)

Checks whether the target JComponent that will be receiving the focus
is ready to accept it.

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

use

shouldYieldFocus(JComponent, JComponent)

instead.

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.

Checks whether the JComponent's input is valid.

Checks whether the target JComponent that will be receiving the focus
is ready to accept it.

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

- InputVerifier

```java
public InputVerifier()
```

============ METHOD DETAIL ==========

- Method Detail

- verify

```java
public abstract boolean verify​(
JComponent
input)
```

Checks whether the JComponent's input is valid. This method should
have no side effects. It returns a boolean indicating the status
of the argument's input.

**Parameters:** input

- the JComponent to verify
**Returns:** true

when valid,

false

when invalid
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

- shouldYieldFocus

```java
@Deprecated
(
since
="9")
public boolean shouldYieldFocus​(
JComponent
input)
```

Deprecated.

use

shouldYieldFocus(JComponent, JComponent)

instead.

Calls

verify(input)

to ensure that the input is valid.
This method can have side effects. In particular, this method
is called when the user attempts to advance focus out of the
argument component into another Swing component in this window.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the argument component.

**Parameters:** input

- the JComponent to verify
**Returns:** true

when valid,

false

when invalid
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

- verifyTarget

```java
public boolean verifyTarget​(
JComponent
target)
```

Checks whether the target JComponent that will be receiving the focus
is ready to accept it. This method should be over-ridden only if it is
necessary to validate the target of the focus transfer.
This method should have no side effects. It returns a boolean
indicating the status of the argument's input.

**Implementation Requirements:** By default this method returns

true

.
**Parameters:** target

- the target JComponent to verify
**Returns:** true

when valid,

false

when invalid
**Since:** 9
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

- shouldYieldFocus

```java
public boolean shouldYieldFocus​(
JComponent
source,

JComponent
target)
```

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.
This method can have side effects.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the first argument component.

**Implementation Requirements:** The basic implementation of this method returns the conjunction
of results obtained from

verify(input)

and

verifyTarget(input)

to ensure that both the source and the target
components are in valid state.
**Parameters:** source

- the source JComponent of the focus transfer
**Parameters:** target

- the target JComponent of the focus transfer
**Returns:** true

when valid,

false

when invalid
**Since:** 9
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

Constructor Detail

- InputVerifier

```java
public InputVerifier()
```

---

#### Constructor Detail

InputVerifier

```java
public InputVerifier()
```

---

#### InputVerifier

public InputVerifier()

Method Detail

- verify

```java
public abstract boolean verify​(
JComponent
input)
```

Checks whether the JComponent's input is valid. This method should
have no side effects. It returns a boolean indicating the status
of the argument's input.

**Parameters:** input

- the JComponent to verify
**Returns:** true

when valid,

false

when invalid
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

- shouldYieldFocus

```java
@Deprecated
(
since
="9")
public boolean shouldYieldFocus​(
JComponent
input)
```

Deprecated.

use

shouldYieldFocus(JComponent, JComponent)

instead.

Calls

verify(input)

to ensure that the input is valid.
This method can have side effects. In particular, this method
is called when the user attempts to advance focus out of the
argument component into another Swing component in this window.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the argument component.

**Parameters:** input

- the JComponent to verify
**Returns:** true

when valid,

false

when invalid
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

- verifyTarget

```java
public boolean verifyTarget​(
JComponent
target)
```

Checks whether the target JComponent that will be receiving the focus
is ready to accept it. This method should be over-ridden only if it is
necessary to validate the target of the focus transfer.
This method should have no side effects. It returns a boolean
indicating the status of the argument's input.

**Implementation Requirements:** By default this method returns

true

.
**Parameters:** target

- the target JComponent to verify
**Returns:** true

when valid,

false

when invalid
**Since:** 9
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

- shouldYieldFocus

```java
public boolean shouldYieldFocus​(
JComponent
source,

JComponent
target)
```

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.
This method can have side effects.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the first argument component.

**Implementation Requirements:** The basic implementation of this method returns the conjunction
of results obtained from

verify(input)

and

verifyTarget(input)

to ensure that both the source and the target
components are in valid state.
**Parameters:** source

- the source JComponent of the focus transfer
**Parameters:** target

- the target JComponent of the focus transfer
**Returns:** true

when valid,

false

when invalid
**Since:** 9
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### Method Detail

verify

```java
public abstract boolean verify​(
JComponent
input)
```

Checks whether the JComponent's input is valid. This method should
have no side effects. It returns a boolean indicating the status
of the argument's input.

**Parameters:** input

- the JComponent to verify
**Returns:** true

when valid,

false

when invalid
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### verify

public abstract boolean verify​(

JComponent

input)

Checks whether the JComponent's input is valid. This method should
have no side effects. It returns a boolean indicating the status
of the argument's input.

shouldYieldFocus

```java
@Deprecated
(
since
="9")
public boolean shouldYieldFocus​(
JComponent
input)
```

Deprecated.

use

shouldYieldFocus(JComponent, JComponent)

instead.

Calls

verify(input)

to ensure that the input is valid.
This method can have side effects. In particular, this method
is called when the user attempts to advance focus out of the
argument component into another Swing component in this window.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the argument component.

**Parameters:** input

- the JComponent to verify
**Returns:** true

when valid,

false

when invalid
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### shouldYieldFocus

@Deprecated

(

since

="9")
public boolean shouldYieldFocus​(

JComponent

input)

Calls

verify(input)

to ensure that the input is valid.
This method can have side effects. In particular, this method
is called when the user attempts to advance focus out of the
argument component into another Swing component in this window.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the argument component.

verifyTarget

```java
public boolean verifyTarget​(
JComponent
target)
```

Checks whether the target JComponent that will be receiving the focus
is ready to accept it. This method should be over-ridden only if it is
necessary to validate the target of the focus transfer.
This method should have no side effects. It returns a boolean
indicating the status of the argument's input.

**Implementation Requirements:** By default this method returns

true

.
**Parameters:** target

- the target JComponent to verify
**Returns:** true

when valid,

false

when invalid
**Since:** 9
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### verifyTarget

public boolean verifyTarget​(

JComponent

target)

Checks whether the target JComponent that will be receiving the focus
is ready to accept it. This method should be over-ridden only if it is
necessary to validate the target of the focus transfer.
This method should have no side effects. It returns a boolean
indicating the status of the argument's input.

shouldYieldFocus

```java
public boolean shouldYieldFocus​(
JComponent
source,

JComponent
target)
```

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.
This method can have side effects.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the first argument component.

**Implementation Requirements:** The basic implementation of this method returns the conjunction
of results obtained from

verify(input)

and

verifyTarget(input)

to ensure that both the source and the target
components are in valid state.
**Parameters:** source

- the source JComponent of the focus transfer
**Parameters:** target

- the target JComponent of the focus transfer
**Returns:** true

when valid,

false

when invalid
**Since:** 9
**See Also:** JComponent.setInputVerifier(javax.swing.InputVerifier)

,

JComponent.getInputVerifier()

---

#### shouldYieldFocus

public boolean shouldYieldFocus​(

JComponent

source,

JComponent

target)

Is called by Swing if this

InputVerifier

is assigned to the

source

Swing component to check whether the requested focus
transfer from the

source

to

target

is allowed.
This method can have side effects.
If this method returns

true

, then the focus is transferred
normally; if it returns

false

, then the focus remains in
the first argument component.

---

