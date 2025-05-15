.. _a4_diy:

===
DIY
===

After completing the lab, the player does DIY.

#. Select **DIY** to begin the do-it-yourself activity.

   .. image:: pictures/0001-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 1 (Select DIY)
      :align: center
      :width: 600px

#. Review the **SOLUTION VALIDATION METHOD** to understand how your DIY is assessed.

   .. image:: pictures/0002-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 2 (Read Validation Method)
      :align: center
      :width: 600px

#. In the **AWS Console** page, find and select **EC2**.

   .. image:: pictures/0003-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 3 (Go to EC2 in Console for DIY)
      :align: center
      :width: 600px

#. Select **Instances**.

   .. image:: pictures/0004-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 4 (Select Instances)
      :align: center
      :width: 600px

#. Select **Security**.

   .. image:: pictures/0005-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 5 (Select Security)
      :align: center
      :width: 600px

#. In **Security groups**, select **DbServerSecurityGroup**.

   .. image:: pictures/0006-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 6 (Select DbServerSecurityGroup)
      :align: center
      :width: 600px

#. In the **Security Groups** interface:

   * Select **Edit inbound rules**.

   .. image:: pictures/0007-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 7 (Edit Inbound Rules)
      :align: center
      :width: 600px

#. In the **Edit inbound rules** interface:

   * For Type, select **MYSQL/Aurora**.
   * For Protocol, select **TCP**.
   * For Port range, enter ``3306``.
   * For Source, choose **Custom**.
   * Then select **Save rules**.

   .. image:: pictures/0008-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 8 (Add Inbound Rule)
      :align: center
      :width: 600px

#. In the **Security groups** view, copy the **Security group name**.

   .. image:: pictures/0009-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 9 (Copy Security Group Name)
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Paste the **Security group name** into the **VALIDATION FORM** in the **Database Security Group name** field.

   .. image:: pictures/00010-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 10 (Paste Security Group Name for Validation)
      :align: center
      :width: 600px

#. Then select **VALIDATE**.

   .. image:: pictures/00011-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 11 (Select VALIDATE)
      :align: center
      :width: 600px

#. On the **VALIDATION MESSAGE**, confirm that "Nice!You have properly configured your security!" appears, indicating the **DIY** is complete. Select **EXIT** to exit.

   .. image:: pictures/00012-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 12 (Validation Success and Exit)
      :align: center
      :width: 600px

#. Congratulations on completing lab 7.

   .. image:: pictures/00013-diy-A4.png
      :alt: Placeholder screenshot for A4 DIY Step 13 (Congratulations)
      :align: center
      :width: 600px
