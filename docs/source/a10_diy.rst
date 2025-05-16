.. _a10_diy:

===
DIY
===

After completing the lab, the player does DIY.

Here’s the full set of steps:

#. In the **AWS Console** interface:

   * Find **Amazon DynamoDB**.
   * Select **Amazon DynamoDB**.

   .. image:: pictures/0001-diy-A10.png
      :alt: AWS Console showing Amazon DynamoDB service.
      :align: center
      :width: 600px

#. In the **DynamoDB** interface:

   * Select **Tables**.
   * Select the **UserVideoHistory** table.
   * Select **Actions**.
   * Select **Create item**.

   .. image:: pictures/0002-diy-A10.png
      :alt: DynamoDB interface navigating to create an item for UserVideoHistory.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * In the **userId** field, enter ``12345-abcd-6785``.

   .. image:: pictures/0003-diy-A10.png
      :alt: Create item interface showing userId entry.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * In the **lastDateWatched** field, enter ``1619156407``.

   .. image:: pictures/0004-diy-A10.png
      :alt: Create item interface showing lastDateWatched entry.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * Select **Add new attribute**.

   .. image:: pictures/0005-diy-A10.png
      :alt: Create item interface showing Add new attribute button.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * Select **Number** for the new attribute type.

   .. image:: pictures/0006-diy-A10.png
      :alt: Create item interface showing Number attribute type selected.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * For **Attribute name**, enter ``Rating``.

   .. image:: pictures/0007-diy-A10.png
      :alt: Create item interface showing Rating attribute name entry.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * For **Value**, enter ``5``.

   .. image:: pictures/0008-diy-A10.png
      :alt: Create item interface showing Rating attribute value entry.
      :align: center
      :width: 600px

#. In the **Create item** interface:

   * Select **Create item**.

   .. image:: pictures/0009-diy-A10.png
      :alt: Create item interface showing Create item button.
      :align: center
      :width: 600px

#. In the **DynamoDB** interface:

   * View the **Items returned** (the new item should be shown).

   .. image:: pictures/00010-diy-A10.png
      :alt: DynamoDB interface showing items returned with the new item.
      :align: center
      :width: 600px

#. In the **Item editor** interface:

   * In the **Attribute name** column, change "Rating" to lowercase ``rating``.

   .. image:: pictures/00011-diy-A10.png
      :alt: Item editor interface showing attribute name being edited to lowercase rating.
      :align: center
      :width: 600px

#. In the **Item editor** interface:

   * Select **Save changes**.

   .. image:: pictures/00012-diy-A10.png
      :alt: Item editor interface showing Save changes button.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Enter **UserVideoHistory** into the **DynamoDB table name** field.
   * Enter **12345-abcd-6785** in the **Item User Id** field.
   * Select **VALIDATE**.

   .. image:: pictures/00013-diy-A10.png
      :alt: DIY interface showing table name and user ID entered for validation.
      :align: center
      :width: 600px
