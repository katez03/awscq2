.. _a5_diy:

===
DIY
===

After completing the lab, the player does DIY.

#. In the **DIY** interface:

   * Review the **DIY ACTIVITIES**.
   * Read the **SOLUTION VALIDATION METHOD**.

   .. image:: pictures/0001-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 1 (Read Goals)
      :align: center
      :width: 600px

#. Navigate to the **AWS Pricing Calculator**.

   .. image:: pictures/0002-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 2 (Go to Pricing Calculator)
      :align: center
      :width: 600px

#. Select **Create estimate**.

   .. image:: pictures/0003-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 3 (Create Estimate)
      :align: center
      :width: 600px

#. In **My Estimate**:

   * Select **Add group**.

   .. image:: pictures/0004-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 4 (Add Group)
      :align: center
      :width: 600px

#. In **Add group**:

   * For Group name, enter **Web Servers**.
   * Then, select **Add group**.

   .. image:: pictures/0005-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 5 (Enter Group Name and Add Group)
      :align: center
      :width: 600px

#. In the **Web Servers** interface:

   * Select **Add service**.

   .. image:: pictures/0006-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 6 (Add Service)
      :align: center
      :width: 600px

#. In **Add service**:

   * Search for **EC2**.
   * Select **Configure**.

   .. image:: pictures/0007-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 7 (Search EC2 and Configure)
      :align: center
      :width: 600px

#. In **Configure Amazon EC2**:

   * For Description, enter **Web Server Estimate**.
   * For Region, select **US East (N. Virginia)**.
   * In **EC2 instance specifications**, select **Linux**.

   .. image:: pictures/0008-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 8 (Configure EC2 Basic)
      :align: center
      :width: 600px

#. In the **Workload** interface:

   * Select **Daily spike traffic**.

   .. image:: pictures/0009-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 9 (Select Workload)
      :align: center
      :width: 600px

#. In the Daily spike pattern, **Workload days** section:

   * Choose the days of the week.

   .. image:: pictures/00010-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 10 (Choose Workload Days)
      :align: center
      :width: 600px

#. In the Daily spike pattern:

   * For Baseline, enter ``2``.
   * For Peak, enter ``4``.
   * For Duration of peak, enter ``8`` and ``0``.

   .. image:: pictures/00011-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 11 (Configure Daily Spike Pattern)
      :align: center
      :width: 600px

#. In **EC2 Instances**:

   * Select **t2.micro**.

   .. image:: pictures/00012-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 12 (Select Instance Type)
      :align: center
      :width: 600px

#. In **Pricing strategy**:

   * For Pricing model, select **On-demand**.
   * Select **Show calculations**.
   * Select **estimate workload hours**.

   .. image:: pictures/00013-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 13 (Configure Pricing Strategy)
      :align: center
      :width: 600px

#. In **Amazon Elastic Block Storage (EBS)**:

   * For Storage for each EC2 instance, select **General Purpose SSD (gp2)**.
   * For Storage amount, enter ``30``.
   * For Snapshot Frequency, enter **Weekly**.
   * For Amount changed per snapshot, enter **1**.

   .. image:: pictures/00014-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 14 (Configure EBS)
      :align: center
      :width: 600px

#. View the results for **Estimated workload hours**.

   .. image:: pictures/00015-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 15 (View Estimated Workload Hours)
      :align: center
      :width: 600px

#. In **Data Transfer**:

   * For Inbound Data Transfer, select **Internet (free)**.
   * Enter ``1``.
   * Select **TB per month**.

   .. image:: pictures/00016-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 16 (Configure Inbound Data Transfer)
      :align: center
      :width: 600px

#. In **Data Transfer**:

   * For Outbound Data Transfer, select **Internet ($0.05 - $0.09 per GB)**.
   * Enter ``100``.
   * Select **TB per month**.

   .. image:: pictures/00017-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 17 (Configure Outbound Data Transfer)
      :align: center
      :width: 600px

#. Select **Show calculations**.

   .. image:: pictures/00018-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 18 (Show Calculations)
      :align: center
      :width: 600px

#. View and select **Add to my estimate**.

   .. image:: pictures/00019-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 19 (Add to My Estimate)
      :align: center
      :width: 600px

#. In the **Web Servers** interface:

   * Select **Share**.

   .. image:: pictures/00020-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 20 (Share Estimate)
      :align: center
      :width: 600px

#. Congratulations to the player on receiving the reward.

   .. image:: pictures/00021-diy-A5.png
      :alt: Placeholder screenshot for A5 DIY Step 21 (Congratulations)
      :align: center
      :width: 600px
