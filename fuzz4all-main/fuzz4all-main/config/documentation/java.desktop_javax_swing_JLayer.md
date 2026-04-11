# Class JLayer<V extends Component >

**Source:** `java.desktop\javax\swing\JLayer.html`

### Class Description

```java
public final class
JLayer<V extends
Component
>

extends
JComponent

implements
Scrollable
,
PropertyChangeListener
,
Accessible
```

JLayer

is a universal decorator for Swing components
which enables you to implement various advanced painting effects as well as
receive notifications of all

AWTEvent

s generated within its borders.

JLayer

delegates the handling of painting and input events to a

LayerUI

object, which performs the actual decoration.

The custom painting implemented in the

LayerUI

and events notification
work for the JLayer itself and all its subcomponents.
This combination enables you to enrich existing components
by adding new advanced functionality such as temporary locking of a hierarchy,
data tips for compound components, enhanced mouse scrolling etc and so on.

JLayer

is a good solution if you only need to do custom painting
over compound component or catch input events from its subcomponents.

```java
import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}
```

Note:

JLayer

doesn't support the following methods:

- Container.add(java.awt.Component)
- Container.add(String, java.awt.Component)
- Container.add(java.awt.Component, int)
- Container.add(java.awt.Component, Object)
- Container.add(java.awt.Component, Object, int)

using any of them will cause

UnsupportedOperationException

to be thrown,
to add a component to

JLayer

use

setView(Component)

or

setGlassPane(JPanel)

.

**Type Parameters:** V

- the type of

JLayer

's view component

---

### Field Details

*No entries found.*

### Constructor Details

#### public JLayer()

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

**See Also:**
- setView(V)

,

setUI(javax.swing.plaf.LayerUI<? super V>)

---

#### public JLayer​(
V
view)

Creates a new

JLayer

object
with default

LayerUI

.

**Parameters:**
- view

- the component to be decorated by this

JLayer

**See Also:**
- setUI(javax.swing.plaf.LayerUI<? super V>)

---

#### public JLayer​(
V
view,

LayerUI
<
V
> ui)

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

**Parameters:**
- view

- the component to be decorated
- ui

- the

LayerUI

delegate
to be used by this

JLayer

---

### Method Details

#### public
V
getView()

Returns the

JLayer

's view component or

null

.

This is a bound property.

**Returns:**
- the

JLayer

's view component
or

null

if none exists

**See Also:**
- setView(Component)

---

#### public void setView​(
V
view)

Sets the

JLayer

's view component, which can be

null

.

This is a bound property.

**Parameters:**
- view

- the view component for this

JLayer

**See Also:**
- getView()

---

#### public void setUI​(
LayerUI
<? super
V
> ui)

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

**Parameters:**
- ui

- the

LayerUI

for this

JLayer

---

#### public
LayerUI
<? super
V
> getUI()

Returns the

LayerUI

for this

JLayer

.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

LayerUI

for this

JLayer

---

#### public
JPanel
getGlassPane()

Returns the

JLayer

's glassPane component or

null

.

This is a bound property.

**Returns:**
- the

JLayer

's glassPane component
or

null

if none exists

**See Also:**
- setGlassPane(JPanel)

---

#### public void setGlassPane​(
JPanel
glassPane)

Sets the

JLayer

's glassPane component, which can be

null

.

This is a bound property.

**Parameters:**
- glassPane

- the glassPane component of this

JLayer

**See Also:**
- getGlassPane()

---

#### public
JPanel
createGlassPane()

Called by the constructor methods to create a default

glassPane

.
By default this method creates a new JPanel with visibility set to true
and opacity set to false.

**Returns:**
- the default

glassPane

---

#### public void setLayout​(
LayoutManager
mgr)

Sets the layout manager for this container. This method is
overridden to prevent the layout manager from being set.

Note: If

mgr

is non-

null

, this
method will throw an exception as layout managers are not supported on
a

JLayer

.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- mgr

- the specified layout manager

**Throws:**
- IllegalArgumentException

- this method is not supported

**See Also:**
- Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### public void setBorder​(
Border
border)

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

**Overrides:**
- setBorder

in class

JComponent

**Parameters:**
- border

- the border to be rendered for the

view

component

**See Also:**
- getView()

,

JComponent.setBorder(Border)

---

#### public
Border
getBorder()

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

**Overrides:**
- getBorder

in class

JComponent

**Returns:**
- the border object for the

view

component

**See Also:**
- getView()

,

setBorder(javax.swing.border.Border)

,

JComponent.getBorder()

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to be added
- constraints

- an object expressing layout constraints
for this component
- index

- the position in the container's list at which to
insert the component, where

-1

means append to the end

**Throws:**
- UnsupportedOperationException

- this method is not supported

**See Also:**
- setView(Component)

,

setGlassPane(JPanel)

---

#### protected boolean isPaintingOrigin()

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

**Overrides:**
- isPaintingOrigin

in class

JComponent

**Returns:**
- true

**See Also:**
- JComponent.isPaintingOrigin()

---

#### public void paintImmediately​(int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

**Overrides:**
- paintImmediately

in class

JComponent

**Parameters:**
- x

- the x value of the region to be painted
- y

- the y value of the region to be painted
- w

- the width of the region to be painted
- h

- the height of the region to be painted

**See Also:**
- JComponent.repaint(long, int, int, int, int)

,

JComponent.isPaintingOrigin()

---

#### public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

**Specified by:**
- imageUpdate

in interface

ImageObserver

**Overrides:**
- imageUpdate

in class

Component

**Parameters:**
- img

- the image being observed
- infoflags

- see

imageUpdate

for more information
- x

- the

x

coordinate
- y

- the

y

coordinate
- w

- the width
- h

- the height

**Returns:**
- false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.

**See Also:**
- ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public void paint​(
Graphics
g)

Delegates all painting to the

LayerUI

object.

**Overrides:**
- paint

in class

JComponent

**Parameters:**
- g

- the

Graphics

to render to

**See Also:**
- JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

#### protected void paintComponent​(
Graphics
g)

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

**Overrides:**
- paintComponent

in class

JComponent

**Parameters:**
- g

- the

Graphics

object to protect

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

ComponentUI

---

#### public boolean isOptimizedDrawingEnabled()

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.
This ensures
that the drawing machinery will call the

JLayer

's

paint

implementation rather than messaging the

JLayer

's
children directly.

**Overrides:**
- isOptimizedDrawingEnabled

in class

JComponent

**Returns:**
- false

---

#### public void setLayerEventMask​(long layerEventMask)

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

Events are delivered provided that

LayerUI

is set
for this

JLayer

and the

JLayer

is displayable.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

**Parameters:**
- layerEventMask

- the bitmask of event types to receive

**See Also:**
- getLayerEventMask()

,

LayerUI.eventDispatched(AWTEvent, JLayer)

,

Component.isDisplayable()

---

#### public long getLayerEventMask()

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

It means that

LayerUI.eventDispatched(AWTEvent, JLayer)

method
will only receive events that match the event mask.

By default

JLayer

receives no events.

**Returns:**
- the bitmask of event types to receive for this

JLayer

---

#### public void updateUI()

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

---

#### public
Dimension
getPreferredScrollableViewportSize()

Returns the preferred size of the viewport for a view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:**
- getPreferredScrollableViewportSize

in interface

Scrollable

**Returns:**
- the preferred size of the viewport for a view component

**See Also:**
- Scrollable

---

#### public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:**
- getScrollableBlockIncrement

in interface

Scrollable

**Parameters:**
- visibleRect

- The view area visible within the viewport
- orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
- direction

- Less than zero to scroll up/left, greater than zero for down/right.

**Returns:**
- the "block" increment for scrolling in the specified direction

**See Also:**
- Scrollable

---

#### public boolean getScrollableTracksViewportHeight()

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:**
- getScrollableTracksViewportHeight

in interface

Scrollable

**Returns:**
- whether the layer should track the height of the viewport

**See Also:**
- Scrollable

---

#### public boolean getScrollableTracksViewportWidth()

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:**
- getScrollableTracksViewportWidth

in interface

Scrollable

**Returns:**
- whether the layer should track the width of the viewport

**See Also:**
- Scrollable

---

#### public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.
Ideally, components should handle a partially exposed row or column
by returning the distance required to completely expose the item.

Scrolling containers, like

JScrollPane

, will use this method
each time the user requests a unit scroll.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:**
- getScrollableUnitIncrement

in interface

Scrollable

**Parameters:**
- visibleRect

- The view area visible within the viewport
- orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
- direction

- Less than zero to scroll up/left, greater than zero for down/right.

**Returns:**
- The "unit" increment for scrolling in the specified direction.
This value should always be positive.

**See Also:**
- Scrollable

---

#### public void doLayout()

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

**Overrides:**
- doLayout

in class

Container

**See Also:**
- LayoutManager.layoutContainer(java.awt.Container)

,

Container.setLayout(java.awt.LayoutManager)

,

Container.validate()

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this

JLayer

.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- the AccessibleContext associated with this

JLayer

.

---

### Additional Sections

#### Class JLayer<V extends Component >

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLayer<V>

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLayer<V>

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JLayer<V>

javax.swing.JComponent

- javax.swing.JLayer<V>

javax.swing.JLayer<V>

**Type Parameters:** V

- the type of

JLayer

's view component

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

PropertyChangeListener

,

Serializable

,

EventListener

,

Accessible

,

Scrollable

```java
public final class
JLayer<V extends
Component
>

extends
JComponent

implements
Scrollable
,
PropertyChangeListener
,
Accessible
```

JLayer

is a universal decorator for Swing components
which enables you to implement various advanced painting effects as well as
receive notifications of all

AWTEvent

s generated within its borders.

JLayer

delegates the handling of painting and input events to a

LayerUI

object, which performs the actual decoration.

The custom painting implemented in the

LayerUI

and events notification
work for the JLayer itself and all its subcomponents.
This combination enables you to enrich existing components
by adding new advanced functionality such as temporary locking of a hierarchy,
data tips for compound components, enhanced mouse scrolling etc and so on.

JLayer

is a good solution if you only need to do custom painting
over compound component or catch input events from its subcomponents.

```java
import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}
```

Note:

JLayer

doesn't support the following methods:

- Container.add(java.awt.Component)
- Container.add(String, java.awt.Component)
- Container.add(java.awt.Component, int)
- Container.add(java.awt.Component, Object)
- Container.add(java.awt.Component, Object, int)

using any of them will cause

UnsupportedOperationException

to be thrown,
to add a component to

JLayer

use

setView(Component)

or

setGlassPane(JPanel)

.

**Since:** 1.7
**See Also:** JLayer(Component)

,

setView(Component)

,

getView()

,

LayerUI

,

JLayer(Component, LayerUI)

,

setUI(javax.swing.plaf.LayerUI)

,

getUI()

,

Serialized Form

public final class

JLayer<V extends

Component

>

extends

JComponent

implements

Scrollable

,

PropertyChangeListener

,

Accessible

JLayer

is a universal decorator for Swing components
which enables you to implement various advanced painting effects as well as
receive notifications of all

AWTEvent

s generated within its borders.

JLayer

delegates the handling of painting and input events to a

LayerUI

object, which performs the actual decoration.

The custom painting implemented in the

LayerUI

and events notification
work for the JLayer itself and all its subcomponents.
This combination enables you to enrich existing components
by adding new advanced functionality such as temporary locking of a hierarchy,
data tips for compound components, enhanced mouse scrolling etc and so on.

JLayer

is a good solution if you only need to do custom painting
over compound component or catch input events from its subcomponents.

```java
import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}
```

Note:

JLayer

doesn't support the following methods:

- Container.add(java.awt.Component)
- Container.add(String, java.awt.Component)
- Container.add(java.awt.Component, int)
- Container.add(java.awt.Component, Object)
- Container.add(java.awt.Component, Object, int)

using any of them will cause

UnsupportedOperationException

to be thrown,
to add a component to

JLayer

use

setView(Component)

or

setGlassPane(JPanel)

.

JLayer

delegates the handling of painting and input events to a

LayerUI

object, which performs the actual decoration.

The custom painting implemented in the

LayerUI

and events notification
work for the JLayer itself and all its subcomponents.
This combination enables you to enrich existing components
by adding new advanced functionality such as temporary locking of a hierarchy,
data tips for compound components, enhanced mouse scrolling etc and so on.

JLayer

is a good solution if you only need to do custom painting
over compound component or catch input events from its subcomponents.

```java
import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}
```

Note:

JLayer

doesn't support the following methods:

- Container.add(java.awt.Component)
- Container.add(String, java.awt.Component)
- Container.add(java.awt.Component, int)
- Container.add(java.awt.Component, Object)
- Container.add(java.awt.Component, Object, int)

using any of them will cause

UnsupportedOperationException

to be thrown,
to add a component to

JLayer

use

setView(Component)

or

setGlassPane(JPanel)

.

The custom painting implemented in the

LayerUI

and events notification
work for the JLayer itself and all its subcomponents.
This combination enables you to enrich existing components
by adding new advanced functionality such as temporary locking of a hierarchy,
data tips for compound components, enhanced mouse scrolling etc and so on.

JLayer

is a good solution if you only need to do custom painting
over compound component or catch input events from its subcomponents.

```java
import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}
```

Note:

JLayer

doesn't support the following methods:

- Container.add(java.awt.Component)
- Container.add(String, java.awt.Component)
- Container.add(java.awt.Component, int)
- Container.add(java.awt.Component, Object)
- Container.add(java.awt.Component, Object, int)

using any of them will cause

UnsupportedOperationException

to be thrown,
to add a component to

JLayer

use

setView(Component)

or

setGlassPane(JPanel)

.

JLayer

is a good solution if you only need to do custom painting
over compound component or catch input events from its subcomponents.

```java
import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}
```

Note:

JLayer

doesn't support the following methods:

- Container.add(java.awt.Component)
- Container.add(String, java.awt.Component)
- Container.add(java.awt.Component, int)
- Container.add(java.awt.Component, Object)
- Container.add(java.awt.Component, Object, int)

using any of them will cause

UnsupportedOperationException

to be thrown,
to add a component to

JLayer

use

setView(Component)

or

setGlassPane(JPanel)

.

import javax.swing.*;
import javax.swing.plaf.LayerUI;
import java.awt.*;

public class JLayerSample {

private static JLayer<JComponent> createLayer() {
// This custom layerUI will fill the layer with translucent green
// and print out all mouseMotion events generated within its borders
LayerUI<JComponent> layerUI = new LayerUI<JComponent>() {

public void paint(Graphics g, JComponent c) {
// paint the layer as is
super.paint(g, c);
// fill it with the translucent green
g.setColor(new Color(0, 128, 0, 128));
g.fillRect(0, 0, c.getWidth(), c.getHeight());
}

public void installUI(JComponent c) {
super.installUI(c);
// enable mouse motion events for the layer's subcomponents
((JLayer) c).setLayerEventMask(AWTEvent.MOUSE_MOTION_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
// reset the layer event mask
((JLayer) c).setLayerEventMask(0);
}

// overridden method which catches MouseMotion events
public void eventDispatched(AWTEvent e, JLayer<? extends JComponent> l) {
System.out.println("AWTEvent detected: " + e);
}
};
// create a component to be decorated with the layer
JPanel panel = new JPanel();
panel.add(new JButton("JButton"));

// create the layer for the panel using our custom layerUI
return new JLayer<JComponent>(panel, layerUI);
}

private static void createAndShowGUI() {
final JFrame frame = new JFrame();
frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

// work with the layer as with any other Swing component
frame.add(createLayer());

frame.setSize(200, 200);
frame.setLocationRelativeTo(null);
frame.setVisible(true);
}

public static void main(String[] args) throws Exception {
SwingUtilities.invokeAndWait(new Runnable() {
public void run() {
createAndShowGUI();
}
});
}
}

Container.add(java.awt.Component)

Container.add(String, java.awt.Component)

Container.add(java.awt.Component, int)

Container.add(java.awt.Component, Object)

Container.add(java.awt.Component, Object, int)

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JLayer

()

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

JLayer

​(

V

view)

Creates a new

JLayer

object
with default

LayerUI

.

JLayer

​(

V

view,

LayerUI

<

V

> ui)

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

JPanel

createGlassPane

()

Called by the constructor methods to create a default

glassPane

.

void

doLayout

()

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this

JLayer

.

Border

getBorder

()

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

JPanel

getGlassPane

()

Returns the

JLayer

's glassPane component or

null

.

long

getLayerEventMask

()

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

Dimension

getPreferredScrollableViewportSize

()

Returns the preferred size of the viewport for a view component.

int

getScrollableBlockIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

boolean

getScrollableTracksViewportHeight

()

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

boolean

getScrollableTracksViewportWidth

()

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

int

getScrollableUnitIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.

LayerUI

<? super

V

>

getUI

()

Returns the

LayerUI

for this

JLayer

.

V

getView

()

Returns the

JLayer

's view component or

null

.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

boolean

isOptimizedDrawingEnabled

()

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.

protected boolean

isPaintingOrigin

()

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

void

paint

​(

Graphics

g)

Delegates all painting to the

LayerUI

object.

protected void

paintComponent

​(

Graphics

g)

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

void

paintImmediately

​(int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

void

setBorder

​(

Border

border)

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

void

setGlassPane

​(

JPanel

glassPane)

Sets the

JLayer

's glassPane component, which can be

null

.

void

setLayerEventMask

​(long layerEventMask)

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container.

void

setUI

​(

LayerUI

<? super

V

> ui)

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

void

setView

​(

V

view)

Sets the

JLayer

's view component, which can be

null

.

void

updateUI

()

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getUIClassID

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isPaintingForPrint

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paintBorder

,

paintChildren

,

paintImmediately

,

paramString

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

wait

,

wait

,

wait

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

JLayer

()

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

JLayer

​(

V

view)

Creates a new

JLayer

object
with default

LayerUI

.

JLayer

​(

V

view,

LayerUI

<

V

> ui)

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

---

#### Constructor Summary

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

Creates a new

JLayer

object
with default

LayerUI

.

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

JPanel

createGlassPane

()

Called by the constructor methods to create a default

glassPane

.

void

doLayout

()

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this

JLayer

.

Border

getBorder

()

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

JPanel

getGlassPane

()

Returns the

JLayer

's glassPane component or

null

.

long

getLayerEventMask

()

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

Dimension

getPreferredScrollableViewportSize

()

Returns the preferred size of the viewport for a view component.

int

getScrollableBlockIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

boolean

getScrollableTracksViewportHeight

()

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

boolean

getScrollableTracksViewportWidth

()

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

int

getScrollableUnitIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.

LayerUI

<? super

V

>

getUI

()

Returns the

LayerUI

for this

JLayer

.

V

getView

()

Returns the

JLayer

's view component or

null

.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

boolean

isOptimizedDrawingEnabled

()

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.

protected boolean

isPaintingOrigin

()

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

void

paint

​(

Graphics

g)

Delegates all painting to the

LayerUI

object.

protected void

paintComponent

​(

Graphics

g)

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

void

paintImmediately

​(int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

void

setBorder

​(

Border

border)

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

void

setGlassPane

​(

JPanel

glassPane)

Sets the

JLayer

's glassPane component, which can be

null

.

void

setLayerEventMask

​(long layerEventMask)

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container.

void

setUI

​(

LayerUI

<? super

V

> ui)

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

void

setView

​(

V

view)

Sets the

JLayer

's view component, which can be

null

.

void

updateUI

()

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getUIClassID

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isPaintingForPrint

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paintBorder

,

paintChildren

,

paintImmediately

,

paramString

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

wait

,

wait

,

wait

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Method Summary

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

Called by the constructor methods to create a default

glassPane

.

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

Gets the AccessibleContext associated with this

JLayer

.

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

Returns the

JLayer

's glassPane component or

null

.

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

Returns the preferred size of the viewport for a view component.

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.

Returns the

LayerUI

for this

JLayer

.

Returns the

JLayer

's view component or

null

.

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

Delegates all painting to the

LayerUI

object.

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

Sets the

JLayer

's glassPane component, which can be

null

.

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

Sets the layout manager for this container.

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

Sets the

JLayer

's view component, which can be

null

.

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getUIClassID

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isPaintingForPrint

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paintBorder

,

paintChildren

,

paintImmediately

,

paramString

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JLayer

```java
public JLayer()
```

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

**See Also:** setView(V)

,

setUI(javax.swing.plaf.LayerUI<? super V>)

- JLayer

```java
public JLayer​(
V
view)
```

Creates a new

JLayer

object
with default

LayerUI

.

**Parameters:** view

- the component to be decorated by this

JLayer
**See Also:** setUI(javax.swing.plaf.LayerUI<? super V>)

- JLayer

```java
public JLayer​(
V
view,

LayerUI
<
V
> ui)
```

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

**Parameters:** view

- the component to be decorated
**Parameters:** ui

- the

LayerUI

delegate
to be used by this

JLayer

============ METHOD DETAIL ==========

- Method Detail

- getView

```java
public
V
getView()
```

Returns the

JLayer

's view component or

null

.

This is a bound property.

**Returns:** the

JLayer

's view component
or

null

if none exists
**See Also:** setView(Component)

- setView

```java
public void setView​(
V
view)
```

Sets the

JLayer

's view component, which can be

null

.

This is a bound property.

**Parameters:** view

- the view component for this

JLayer
**See Also:** getView()

- setUI

```java
public void setUI​(
LayerUI
<? super
V
> ui)
```

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

**Parameters:** ui

- the

LayerUI

for this

JLayer

- getUI

```java
public
LayerUI
<? super
V
> getUI()
```

Returns the

LayerUI

for this

JLayer

.

**Overrides:** getUI

in class

JComponent
**Returns:** the

LayerUI

for this

JLayer

- getGlassPane

```java
public
JPanel
getGlassPane()
```

Returns the

JLayer

's glassPane component or

null

.

This is a bound property.

**Returns:** the

JLayer

's glassPane component
or

null

if none exists
**See Also:** setGlassPane(JPanel)

- setGlassPane

```java
public void setGlassPane​(
JPanel
glassPane)
```

Sets the

JLayer

's glassPane component, which can be

null

.

This is a bound property.

**Parameters:** glassPane

- the glassPane component of this

JLayer
**See Also:** getGlassPane()

- createGlassPane

```java
public
JPanel
createGlassPane()
```

Called by the constructor methods to create a default

glassPane

.
By default this method creates a new JPanel with visibility set to true
and opacity set to false.

**Returns:** the default

glassPane

- setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container. This method is
overridden to prevent the layout manager from being set.

Note: If

mgr

is non-

null

, this
method will throw an exception as layout managers are not supported on
a

JLayer

.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**Throws:** IllegalArgumentException

- this method is not supported
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- setBorder

```java
public void setBorder​(
Border
border)
```

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

**Overrides:** setBorder

in class

JComponent
**Parameters:** border

- the border to be rendered for the

view

component
**See Also:** getView()

,

JComponent.setBorder(Border)

- getBorder

```java
public
Border
getBorder()
```

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

**Overrides:** getBorder

in class

JComponent
**Returns:** the border object for the

view

component
**See Also:** getView()

,

setBorder(javax.swing.border.Border)

,

JComponent.getBorder()

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** UnsupportedOperationException

- this method is not supported
**See Also:** setView(Component)

,

setGlassPane(JPanel)

- isPaintingOrigin

```java
protected boolean isPaintingOrigin()
```

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

**Overrides:** isPaintingOrigin

in class

JComponent
**Returns:** true
**See Also:** JComponent.isPaintingOrigin()

- paintImmediately

```java
public void paintImmediately​(int x,
int y,
int w,
int h)
```

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

**Overrides:** paintImmediately

in class

JComponent
**Parameters:** x

- the x value of the region to be painted
**Parameters:** y

- the y value of the region to be painted
**Parameters:** w

- the width of the region to be painted
**Parameters:** h

- the height of the region to be painted
**See Also:** JComponent.repaint(long, int, int, int, int)

,

JComponent.isPaintingOrigin()

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- paint

```java
public void paint​(
Graphics
g)
```

Delegates all painting to the

LayerUI

object.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

to render to
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

- paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

object to protect
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

- isOptimizedDrawingEnabled

```java
public boolean isOptimizedDrawingEnabled()
```

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.
This ensures
that the drawing machinery will call the

JLayer

's

paint

implementation rather than messaging the

JLayer

's
children directly.

**Overrides:** isOptimizedDrawingEnabled

in class

JComponent
**Returns:** false

- setLayerEventMask

```java
public void setLayerEventMask​(long layerEventMask)
```

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

Events are delivered provided that

LayerUI

is set
for this

JLayer

and the

JLayer

is displayable.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

**Parameters:** layerEventMask

- the bitmask of event types to receive
**See Also:** getLayerEventMask()

,

LayerUI.eventDispatched(AWTEvent, JLayer)

,

Component.isDisplayable()

- getLayerEventMask

```java
public long getLayerEventMask()
```

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

It means that

LayerUI.eventDispatched(AWTEvent, JLayer)

method
will only receive events that match the event mask.

By default

JLayer

receives no events.

**Returns:** the bitmask of event types to receive for this

JLayer

- updateUI

```java
public void updateUI()
```

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

- getPreferredScrollableViewportSize

```java
public
Dimension
getPreferredScrollableViewportSize()
```

Returns the preferred size of the viewport for a view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getPreferredScrollableViewportSize

in interface

Scrollable
**Returns:** the preferred size of the viewport for a view component
**See Also:** Scrollable

- getScrollableBlockIncrement

```java
public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableBlockIncrement

in interface

Scrollable
**Parameters:** visibleRect

- The view area visible within the viewport
**Parameters:** orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
**Parameters:** direction

- Less than zero to scroll up/left, greater than zero for down/right.
**Returns:** the "block" increment for scrolling in the specified direction
**See Also:** Scrollable

- getScrollableTracksViewportHeight

```java
public boolean getScrollableTracksViewportHeight()
```

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Returns:** whether the layer should track the height of the viewport
**See Also:** Scrollable

- getScrollableTracksViewportWidth

```java
public boolean getScrollableTracksViewportWidth()
```

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Returns:** whether the layer should track the width of the viewport
**See Also:** Scrollable

- getScrollableUnitIncrement

```java
public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.
Ideally, components should handle a partially exposed row or column
by returning the distance required to completely expose the item.

Scrolling containers, like

JScrollPane

, will use this method
each time the user requests a unit scroll.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableUnitIncrement

in interface

Scrollable
**Parameters:** visibleRect

- The view area visible within the viewport
**Parameters:** orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
**Parameters:** direction

- Less than zero to scroll up/left, greater than zero for down/right.
**Returns:** The "unit" increment for scrolling in the specified direction.
This value should always be positive.
**See Also:** Scrollable

- doLayout

```java
public void doLayout()
```

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

**Overrides:** doLayout

in class

Container
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

,

Container.setLayout(java.awt.LayoutManager)

,

Container.validate()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this

JLayer

.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the AccessibleContext associated with this

JLayer

.

Constructor Detail

- JLayer

```java
public JLayer()
```

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

**See Also:** setView(V)

,

setUI(javax.swing.plaf.LayerUI<? super V>)

- JLayer

```java
public JLayer​(
V
view)
```

Creates a new

JLayer

object
with default

LayerUI

.

**Parameters:** view

- the component to be decorated by this

JLayer
**See Also:** setUI(javax.swing.plaf.LayerUI<? super V>)

- JLayer

```java
public JLayer​(
V
view,

LayerUI
<
V
> ui)
```

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

**Parameters:** view

- the component to be decorated
**Parameters:** ui

- the

LayerUI

delegate
to be used by this

JLayer

---

#### Constructor Detail

JLayer

```java
public JLayer()
```

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

**See Also:** setView(V)

,

setUI(javax.swing.plaf.LayerUI<? super V>)

---

#### JLayer

public JLayer()

Creates a new

JLayer

object with a

null

view component
and default

LayerUI

.

JLayer

```java
public JLayer​(
V
view)
```

Creates a new

JLayer

object
with default

LayerUI

.

**Parameters:** view

- the component to be decorated by this

JLayer
**See Also:** setUI(javax.swing.plaf.LayerUI<? super V>)

---

#### JLayer

public JLayer​(

V

view)

Creates a new

JLayer

object
with default

LayerUI

.

JLayer

```java
public JLayer​(
V
view,

LayerUI
<
V
> ui)
```

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

**Parameters:** view

- the component to be decorated
**Parameters:** ui

- the

LayerUI

delegate
to be used by this

JLayer

---

#### JLayer

public JLayer​(

V

view,

LayerUI

<

V

> ui)

Creates a new

JLayer

object with the specified view component
and

LayerUI

object.

Method Detail

- getView

```java
public
V
getView()
```

Returns the

JLayer

's view component or

null

.

This is a bound property.

**Returns:** the

JLayer

's view component
or

null

if none exists
**See Also:** setView(Component)

- setView

```java
public void setView​(
V
view)
```

Sets the

JLayer

's view component, which can be

null

.

This is a bound property.

**Parameters:** view

- the view component for this

JLayer
**See Also:** getView()

- setUI

```java
public void setUI​(
LayerUI
<? super
V
> ui)
```

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

**Parameters:** ui

- the

LayerUI

for this

JLayer

- getUI

```java
public
LayerUI
<? super
V
> getUI()
```

Returns the

LayerUI

for this

JLayer

.

**Overrides:** getUI

in class

JComponent
**Returns:** the

LayerUI

for this

JLayer

- getGlassPane

```java
public
JPanel
getGlassPane()
```

Returns the

JLayer

's glassPane component or

null

.

This is a bound property.

**Returns:** the

JLayer

's glassPane component
or

null

if none exists
**See Also:** setGlassPane(JPanel)

- setGlassPane

```java
public void setGlassPane​(
JPanel
glassPane)
```

Sets the

JLayer

's glassPane component, which can be

null

.

This is a bound property.

**Parameters:** glassPane

- the glassPane component of this

JLayer
**See Also:** getGlassPane()

- createGlassPane

```java
public
JPanel
createGlassPane()
```

Called by the constructor methods to create a default

glassPane

.
By default this method creates a new JPanel with visibility set to true
and opacity set to false.

**Returns:** the default

glassPane

- setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container. This method is
overridden to prevent the layout manager from being set.

Note: If

mgr

is non-

null

, this
method will throw an exception as layout managers are not supported on
a

JLayer

.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**Throws:** IllegalArgumentException

- this method is not supported
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- setBorder

```java
public void setBorder​(
Border
border)
```

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

**Overrides:** setBorder

in class

JComponent
**Parameters:** border

- the border to be rendered for the

view

component
**See Also:** getView()

,

JComponent.setBorder(Border)

- getBorder

```java
public
Border
getBorder()
```

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

**Overrides:** getBorder

in class

JComponent
**Returns:** the border object for the

view

component
**See Also:** getView()

,

setBorder(javax.swing.border.Border)

,

JComponent.getBorder()

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** UnsupportedOperationException

- this method is not supported
**See Also:** setView(Component)

,

setGlassPane(JPanel)

- isPaintingOrigin

```java
protected boolean isPaintingOrigin()
```

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

**Overrides:** isPaintingOrigin

in class

JComponent
**Returns:** true
**See Also:** JComponent.isPaintingOrigin()

- paintImmediately

```java
public void paintImmediately​(int x,
int y,
int w,
int h)
```

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

**Overrides:** paintImmediately

in class

JComponent
**Parameters:** x

- the x value of the region to be painted
**Parameters:** y

- the y value of the region to be painted
**Parameters:** w

- the width of the region to be painted
**Parameters:** h

- the height of the region to be painted
**See Also:** JComponent.repaint(long, int, int, int, int)

,

JComponent.isPaintingOrigin()

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- paint

```java
public void paint​(
Graphics
g)
```

Delegates all painting to the

LayerUI

object.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

to render to
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

- paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

object to protect
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

- isOptimizedDrawingEnabled

```java
public boolean isOptimizedDrawingEnabled()
```

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.
This ensures
that the drawing machinery will call the

JLayer

's

paint

implementation rather than messaging the

JLayer

's
children directly.

**Overrides:** isOptimizedDrawingEnabled

in class

JComponent
**Returns:** false

- setLayerEventMask

```java
public void setLayerEventMask​(long layerEventMask)
```

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

Events are delivered provided that

LayerUI

is set
for this

JLayer

and the

JLayer

is displayable.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

**Parameters:** layerEventMask

- the bitmask of event types to receive
**See Also:** getLayerEventMask()

,

LayerUI.eventDispatched(AWTEvent, JLayer)

,

Component.isDisplayable()

- getLayerEventMask

```java
public long getLayerEventMask()
```

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

It means that

LayerUI.eventDispatched(AWTEvent, JLayer)

method
will only receive events that match the event mask.

By default

JLayer

receives no events.

**Returns:** the bitmask of event types to receive for this

JLayer

- updateUI

```java
public void updateUI()
```

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

- getPreferredScrollableViewportSize

```java
public
Dimension
getPreferredScrollableViewportSize()
```

Returns the preferred size of the viewport for a view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getPreferredScrollableViewportSize

in interface

Scrollable
**Returns:** the preferred size of the viewport for a view component
**See Also:** Scrollable

- getScrollableBlockIncrement

```java
public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableBlockIncrement

in interface

Scrollable
**Parameters:** visibleRect

- The view area visible within the viewport
**Parameters:** orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
**Parameters:** direction

- Less than zero to scroll up/left, greater than zero for down/right.
**Returns:** the "block" increment for scrolling in the specified direction
**See Also:** Scrollable

- getScrollableTracksViewportHeight

```java
public boolean getScrollableTracksViewportHeight()
```

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Returns:** whether the layer should track the height of the viewport
**See Also:** Scrollable

- getScrollableTracksViewportWidth

```java
public boolean getScrollableTracksViewportWidth()
```

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Returns:** whether the layer should track the width of the viewport
**See Also:** Scrollable

- getScrollableUnitIncrement

```java
public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.
Ideally, components should handle a partially exposed row or column
by returning the distance required to completely expose the item.

Scrolling containers, like

JScrollPane

, will use this method
each time the user requests a unit scroll.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableUnitIncrement

in interface

Scrollable
**Parameters:** visibleRect

- The view area visible within the viewport
**Parameters:** orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
**Parameters:** direction

- Less than zero to scroll up/left, greater than zero for down/right.
**Returns:** The "unit" increment for scrolling in the specified direction.
This value should always be positive.
**See Also:** Scrollable

- doLayout

```java
public void doLayout()
```

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

**Overrides:** doLayout

in class

Container
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

,

Container.setLayout(java.awt.LayoutManager)

,

Container.validate()

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this

JLayer

.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the AccessibleContext associated with this

JLayer

.

---

#### Method Detail

getView

```java
public
V
getView()
```

Returns the

JLayer

's view component or

null

.

This is a bound property.

**Returns:** the

JLayer

's view component
or

null

if none exists
**See Also:** setView(Component)

---

#### getView

public

V

getView()

Returns the

JLayer

's view component or

null

.

This is a bound property.

setView

```java
public void setView​(
V
view)
```

Sets the

JLayer

's view component, which can be

null

.

This is a bound property.

**Parameters:** view

- the view component for this

JLayer
**See Also:** getView()

---

#### setView

public void setView​(

V

view)

Sets the

JLayer

's view component, which can be

null

.

This is a bound property.

setUI

```java
public void setUI​(
LayerUI
<? super
V
> ui)
```

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

**Parameters:** ui

- the

LayerUI

for this

JLayer

---

#### setUI

public void setUI​(

LayerUI

<? super

V

> ui)

Sets the

LayerUI

which will perform painting
and receive input events for this

JLayer

.

getUI

```java
public
LayerUI
<? super
V
> getUI()
```

Returns the

LayerUI

for this

JLayer

.

**Overrides:** getUI

in class

JComponent
**Returns:** the

LayerUI

for this

JLayer

---

#### getUI

public

LayerUI

<? super

V

> getUI()

Returns the

LayerUI

for this

JLayer

.

getGlassPane

```java
public
JPanel
getGlassPane()
```

Returns the

JLayer

's glassPane component or

null

.

This is a bound property.

**Returns:** the

JLayer

's glassPane component
or

null

if none exists
**See Also:** setGlassPane(JPanel)

---

#### getGlassPane

public

JPanel

getGlassPane()

Returns the

JLayer

's glassPane component or

null

.

This is a bound property.

setGlassPane

```java
public void setGlassPane​(
JPanel
glassPane)
```

Sets the

JLayer

's glassPane component, which can be

null

.

This is a bound property.

**Parameters:** glassPane

- the glassPane component of this

JLayer
**See Also:** getGlassPane()

---

#### setGlassPane

public void setGlassPane​(

JPanel

glassPane)

Sets the

JLayer

's glassPane component, which can be

null

.

This is a bound property.

createGlassPane

```java
public
JPanel
createGlassPane()
```

Called by the constructor methods to create a default

glassPane

.
By default this method creates a new JPanel with visibility set to true
and opacity set to false.

**Returns:** the default

glassPane

---

#### createGlassPane

public

JPanel

createGlassPane()

Called by the constructor methods to create a default

glassPane

.
By default this method creates a new JPanel with visibility set to true
and opacity set to false.

setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container. This method is
overridden to prevent the layout manager from being set.

Note: If

mgr

is non-

null

, this
method will throw an exception as layout managers are not supported on
a

JLayer

.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**Throws:** IllegalArgumentException

- this method is not supported
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### setLayout

public void setLayout​(

LayoutManager

mgr)

Sets the layout manager for this container. This method is
overridden to prevent the layout manager from being set.

Note: If

mgr

is non-

null

, this
method will throw an exception as layout managers are not supported on
a

JLayer

.

Note: If

mgr

is non-

null

, this
method will throw an exception as layout managers are not supported on
a

JLayer

.

setBorder

```java
public void setBorder​(
Border
border)
```

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

**Overrides:** setBorder

in class

JComponent
**Parameters:** border

- the border to be rendered for the

view

component
**See Also:** getView()

,

JComponent.setBorder(Border)

---

#### setBorder

public void setBorder​(

Border

border)

Delegates its functionality to the

getView().setBorder(Border)

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise this method is a no-op.

getBorder

```java
public
Border
getBorder()
```

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

**Overrides:** getBorder

in class

JComponent
**Returns:** the border object for the

view

component
**See Also:** getView()

,

setBorder(javax.swing.border.Border)

,

JComponent.getBorder()

---

#### getBorder

public

Border

getBorder()

Delegates its functionality to the

getView().getBorder()

method,
if the view component is an instance of

javax.swing.JComponent

,
otherwise returns

null

.

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** UnsupportedOperationException

- this method is not supported
**See Also:** setView(Component)

,

setGlassPane(JPanel)

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

This method is not supported by

JLayer

and always throws

UnsupportedOperationException

isPaintingOrigin

```java
protected boolean isPaintingOrigin()
```

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

**Overrides:** isPaintingOrigin

in class

JComponent
**Returns:** true
**See Also:** JComponent.isPaintingOrigin()

---

#### isPaintingOrigin

protected boolean isPaintingOrigin()

Always returns

true

to cause painting to originate from

JLayer

,
or one of its ancestors.

paintImmediately

```java
public void paintImmediately​(int x,
int y,
int w,
int h)
```

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

**Overrides:** paintImmediately

in class

JComponent
**Parameters:** x

- the x value of the region to be painted
**Parameters:** y

- the y value of the region to be painted
**Parameters:** w

- the width of the region to be painted
**Parameters:** h

- the height of the region to be painted
**See Also:** JComponent.repaint(long, int, int, int, int)

,

JComponent.isPaintingOrigin()

---

#### paintImmediately

public void paintImmediately​(int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.paintImmediately(int, int, int, int, JLayer)

method,
if

LayerUI

is set.

imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**See Also:** ImageObserver

,

Graphics.drawImage(Image, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, Color, java.awt.image.ImageObserver)

,

Graphics.drawImage(Image, int, int, int, int, java.awt.image.ImageObserver)

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### imageUpdate

public boolean imageUpdate​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

Delegates its functionality to the

LayerUI.imageUpdate(java.awt.Image, int, int, int, int, int, JLayer)

method,
if the

LayerUI

is set.

paint

```java
public void paint​(
Graphics
g)
```

Delegates all painting to the

LayerUI

object.

**Overrides:** paint

in class

JComponent
**Parameters:** g

- the

Graphics

to render to
**See Also:** JComponent.paintComponent(java.awt.Graphics)

,

JComponent.paintBorder(java.awt.Graphics)

,

JComponent.paintChildren(java.awt.Graphics)

,

JComponent.getComponentGraphics(java.awt.Graphics)

,

JComponent.repaint(long, int, int, int, int)

---

#### paint

public void paint​(

Graphics

g)

Delegates all painting to the

LayerUI

object.

paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

object to protect
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

---

#### paintComponent

protected void paintComponent​(

Graphics

g)

This method is empty, because all painting is done by

paint(Graphics)

and

ComponentUI.update(Graphics, JComponent)

methods

isOptimizedDrawingEnabled

```java
public boolean isOptimizedDrawingEnabled()
```

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.
This ensures
that the drawing machinery will call the

JLayer

's

paint

implementation rather than messaging the

JLayer

's
children directly.

**Overrides:** isOptimizedDrawingEnabled

in class

JComponent
**Returns:** false

---

#### isOptimizedDrawingEnabled

public boolean isOptimizedDrawingEnabled()

The

JLayer

overrides the default implementation of
this method (in

JComponent

) to return

false

.
This ensures
that the drawing machinery will call the

JLayer

's

paint

implementation rather than messaging the

JLayer

's
children directly.

setLayerEventMask

```java
public void setLayerEventMask​(long layerEventMask)
```

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

Events are delivered provided that

LayerUI

is set
for this

JLayer

and the

JLayer

is displayable.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

**Parameters:** layerEventMask

- the bitmask of event types to receive
**See Also:** getLayerEventMask()

,

LayerUI.eventDispatched(AWTEvent, JLayer)

,

Component.isDisplayable()

---

#### setLayerEventMask

public void setLayerEventMask​(long layerEventMask)

Enables the events from JLayer and

all its descendants

defined by the specified event mask parameter
to be delivered to the

LayerUI.eventDispatched(AWTEvent, JLayer)

method.

Events are delivered provided that

LayerUI

is set
for this

JLayer

and the

JLayer

is displayable.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

Events are delivered provided that

LayerUI

is set
for this

JLayer

and the

JLayer

is displayable.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

The following example shows how to correctly use this method
in the

LayerUI

implementations:

```java
public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}
```

By default

JLayer

receives no events and its event mask is

0

.

public void installUI(JComponent c) {
super.installUI(c);
JLayer l = (JLayer) c;
// this LayerUI will receive only key and focus events
l.setLayerEventMask(AWTEvent.KEY_EVENT_MASK | AWTEvent.FOCUS_EVENT_MASK);
}

public void uninstallUI(JComponent c) {
super.uninstallUI(c);
JLayer l = (JLayer) c;
// JLayer must be returned to its initial state
l.setLayerEventMask(0);
}

getLayerEventMask

```java
public long getLayerEventMask()
```

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

It means that

LayerUI.eventDispatched(AWTEvent, JLayer)

method
will only receive events that match the event mask.

By default

JLayer

receives no events.

**Returns:** the bitmask of event types to receive for this

JLayer

---

#### getLayerEventMask

public long getLayerEventMask()

Returns the bitmap of event mask to receive by this

JLayer

and its

LayerUI

.

It means that

LayerUI.eventDispatched(AWTEvent, JLayer)

method
will only receive events that match the event mask.

By default

JLayer

receives no events.

It means that

LayerUI.eventDispatched(AWTEvent, JLayer)

method
will only receive events that match the event mask.

By default

JLayer

receives no events.

By default

JLayer

receives no events.

updateUI

```java
public void updateUI()
```

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

---

#### updateUI

public void updateUI()

Delegates its functionality to the

LayerUI.updateUI(JLayer)

method,
if

LayerUI

is set.

getPreferredScrollableViewportSize

```java
public
Dimension
getPreferredScrollableViewportSize()
```

Returns the preferred size of the viewport for a view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getPreferredScrollableViewportSize

in interface

Scrollable
**Returns:** the preferred size of the viewport for a view component
**See Also:** Scrollable

---

#### getPreferredScrollableViewportSize

public

Dimension

getPreferredScrollableViewportSize()

Returns the preferred size of the viewport for a view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

getScrollableBlockIncrement

```java
public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableBlockIncrement

in interface

Scrollable
**Parameters:** visibleRect

- The view area visible within the viewport
**Parameters:** orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
**Parameters:** direction

- Less than zero to scroll up/left, greater than zero for down/right.
**Returns:** the "block" increment for scrolling in the specified direction
**See Also:** Scrollable

---

#### getScrollableBlockIncrement

public int getScrollableBlockIncrement​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one block of rows or columns, depending on the value of orientation.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

getScrollableTracksViewportHeight

```java
public boolean getScrollableTracksViewportHeight()
```

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Returns:** whether the layer should track the height of the viewport
**See Also:** Scrollable

---

#### getScrollableTracksViewportHeight

public boolean getScrollableTracksViewportHeight()

Returns

false

to indicate that the height of the viewport does not
determine the height of the layer, unless the preferred height
of the layer is smaller than the height of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

getScrollableTracksViewportWidth

```java
public boolean getScrollableTracksViewportWidth()
```

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Returns:** whether the layer should track the width of the viewport
**See Also:** Scrollable

---

#### getScrollableTracksViewportWidth

public boolean getScrollableTracksViewportWidth()

Returns

false

to indicate that the width of the viewport does not
determine the width of the layer, unless the preferred width
of the layer is smaller than the width of the viewport.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

getScrollableUnitIncrement

```java
public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.
Ideally, components should handle a partially exposed row or column
by returning the distance required to completely expose the item.

Scrolling containers, like

JScrollPane

, will use this method
each time the user requests a unit scroll.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

**Specified by:** getScrollableUnitIncrement

in interface

Scrollable
**Parameters:** visibleRect

- The view area visible within the viewport
**Parameters:** orientation

- Either SwingConstants.VERTICAL or SwingConstants.HORIZONTAL.
**Parameters:** direction

- Less than zero to scroll up/left, greater than zero for down/right.
**Returns:** The "unit" increment for scrolling in the specified direction.
This value should always be positive.
**See Also:** Scrollable

---

#### getScrollableUnitIncrement

public int getScrollableUnitIncrement​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns a scroll increment, which is required for components
that display logical rows or columns in order to completely expose
one new row or column, depending on the value of orientation.
Ideally, components should handle a partially exposed row or column
by returning the distance required to completely expose the item.

Scrolling containers, like

JScrollPane

, will use this method
each time the user requests a unit scroll.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

Scrolling containers, like

JScrollPane

, will use this method
each time the user requests a unit scroll.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

If the view component of this layer implements

Scrollable

, this method delegates its
implementation to the view component.

doLayout

```java
public void doLayout()
```

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

**Overrides:** doLayout

in class

Container
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

,

Container.setLayout(java.awt.LayoutManager)

,

Container.validate()

---

#### doLayout

public void doLayout()

Delegates its functionality to the

LayerUI.doLayout(JLayer)

method,
if

LayerUI

is set.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this

JLayer

.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the AccessibleContext associated with this

JLayer

.

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this

JLayer

.

---

